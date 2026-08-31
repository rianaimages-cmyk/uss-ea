import io
import json
import os
import hashlib
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
s.headers.update({"User-Agent": "Mozilla/5.0 (compatible; USS-website-asset-refresh/1.0)"})

manifest = []
thumbs = []

for name, page_url in ASSETS.items():
    print(f"Fetching metadata: {name} -> {page_url}")
    meta = s.get("https://api.microlink.io/", params={"url": page_url}, timeout=90)
    meta.raise_for_status()
    payload = meta.json()
    if payload.get("status") != "success":
        raise RuntimeError(f"Microlink failed for {page_url}: {payload}")
    data = payload.get("data", {})
    image = data.get("image")
    image_url = image.get("url") if isinstance(image, dict) else image
    if not image_url:
        raise RuntimeError(f"No primary image returned for {page_url}. Data keys: {list(data)}")

    print(f"Downloading image: {image_url}")
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
        "title": data.get("title"),
        "description": data.get("description"),
    })

(OUT / "manifest.json").write_text(json.dumps(manifest, indent=2), encoding="utf-8")

# Contact sheet for visual QA.
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
