import io
import json
import re
import hashlib
from html import unescape
from pathlib import Path

import requests
from PIL import Image, ImageOps, ImageDraw

ASSETS = {
    "hero-security": "https://www.magnific.com/free-photo/security-camera-urban-video_1270291.htm",
    "control-room-guard": "https://www.magnific.com/free-photo/portrait-male-security-guard-with-radio-station-camera-screens_41554803.htm",
    "security-guard": "https://www.magnific.com/free-photo/portrait-male-security-guard-with-uniform_41554901.htm",
    "cctv-camera-a": "https://www.magnific.com/free-photo/cctv-security-camera_1120820.htm",
    "cctv-camera-b": "https://www.magnific.com/free-photo/cctv-security-camera_1120808.htm",
    "parking-garage": "https://www.magnific.com/free-photo/empty-underground-parking-garage_1175788.htm",
    "parking-ramp": "https://www.magnific.com/free-photo/circular-ramp-parking-garage_1120069.htm",
    "parking-barrier": "https://www.magnific.com/free-vector/parking-security-entrance-with-automatic-car-barrier_15310359.htm",
    "server-room": "https://www.magnific.com/free-photo/corridor-server-room-data-center_31177856.htm",
    "server-technician": "https://www.magnific.com/free-photo/man-doing-tech-support-server-room-managing-large-scale-it-infrastructure-rackmounts-data-center_423708147.htm",
    "meeting-room": "https://www.magnific.com/free-photo/meeting-room-office_19100862.htm",
    "boardroom-team": "https://www.magnific.com/free-photo/corporate-business-people-meeting-boardroom-african-manager-brainstorming-with-colleagues-discussing-strategy-sharing-problem-solving-ideas-collaborating-conference-room-company_17983370.htm",
}

OUT = Path("magnific_assets")
OUT.mkdir(exist_ok=True)

s = requests.Session()
s.headers.update({
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 Chrome/151 Safari/537.36",
    "Accept-Language": "en-US,en;q=0.9",
})


def meta_content(html, key):
    patterns = [
        rf'<meta[^>]+property=["\']{re.escape(key)}["\'][^>]+content=["\']([^"\']+)["\']',
        rf'<meta[^>]+content=["\']([^"\']+)["\'][^>]+property=["\']{re.escape(key)}["\']',
        rf'<meta[^>]+name=["\']{re.escape(key)}["\'][^>]+content=["\']([^"\']+)["\']',
        rf'<meta[^>]+content=["\']([^"\']+)["\'][^>]+name=["\']{re.escape(key)}["\']',
    ]
    for pat in patterns:
        m = re.search(pat, html, flags=re.I)
        if m:
            return unescape(m.group(1))
    return None


def first_http(value):
    if not value:
        return None
    if isinstance(value, str):
        return value if value.startswith("http") else None
    if isinstance(value, dict):
        for key in ("url", "src", "href"):
            v = value.get(key)
            if isinstance(v, str) and v.startswith("http"):
                return v
        for v in value.values():
            got = first_http(v)
            if got:
                return got
    if isinstance(value, list):
        for v in value:
            got = first_http(v)
            if got:
                return got
    return None

manifest = []
thumbs = []

for name, page_url in ASSETS.items():
    print(f"Fetching Magnific page: {name} -> {page_url}")
    page = s.get(page_url, timeout=90)
    page.raise_for_status()
    html = page.text

    image_url = (
        meta_content(html, "og:image")
        or meta_content(html, "twitter:image")
        or meta_content(html, "twitter:image:src")
    )
    title = meta_content(html, "og:title") or meta_content(html, "twitter:title")
    description = meta_content(html, "og:description") or meta_content(html, "description")

    # Fallback to Microlink metadata when page metadata is dynamically rendered.
    if not image_url:
        print("No static OG image; trying Microlink metadata")
        meta = s.get("https://api.microlink.io/", params={"url": page_url}, timeout=90)
        meta.raise_for_status()
        payload = meta.json()
        data = payload.get("data", {}) if payload.get("status") == "success" else {}
        image_url = first_http(data.get("image"))
        title = title or data.get("title")
        description = description or data.get("description")

    if not image_url:
        # Last fallback: Magnific/Freepik pages often expose image URLs in JSON state.
        candidates = re.findall(r'https:\\/\\/[^"\']+?(?:\.jpg|\.jpeg|\.png|\.webp)(?:\?[^"\']*)?', html, flags=re.I)
        candidates = [unescape(c.replace('\\/','/')) for c in candidates]
        candidates = [c for c in candidates if 'magnific' in c or 'freepik' in c or 'img.' in c]
        image_url = candidates[0] if candidates else None

    if not image_url:
        raise RuntimeError(f"No primary image found for {page_url}")

    print(f"Downloading preview image: {image_url}")
    r = s.get(image_url, timeout=120)
    r.raise_for_status()
    raw = r.content
    sha = hashlib.sha256(raw).hexdigest()

    img = Image.open(io.BytesIO(raw))
    img = ImageOps.exif_transpose(img).convert("RGB")
    original_size = img.size
    if max(img.size) > 1800:
        img.thumbnail((1800, 1800), Image.Resampling.LANCZOS)

    out_path = OUT / f"{name}.webp"
    img.save(out_path, "WEBP", quality=88, method=6)

    preview = ImageOps.fit(img, (320, 220), method=Image.Resampling.LANCZOS)
    thumbs.append((name, preview.copy()))
    manifest.append({
        "name": name,
        "magnific_page": page_url,
        "source_image_url": image_url,
        "original_size": original_size,
        "saved_size": img.size,
        "sha256_source": sha,
        "file": out_path.name,
        "title": title,
        "description": description,
    })

(OUT / "manifest.json").write_text(json.dumps(manifest, indent=2), encoding="utf-8")

cols = 3
cell_w, cell_h = 340, 260
rows = (len(thumbs) + cols - 1) // cols
sheet = Image.new("RGB", (cols * cell_w, rows * cell_h), "white")
draw = ImageDraw.Draw(sheet)
for i, (name, thumb) in enumerate(thumbs):
    x = (i % cols) * cell_w + 10
    y = (i // cols) * cell_h + 10
    sheet.paste(thumb, (x, y))
    draw.text((x, y + 225), name, fill="black")
sheet.save(OUT / "contact-sheet.jpg", quality=90)

print(f"Saved {len(manifest)} Magnific assets to {OUT}")
