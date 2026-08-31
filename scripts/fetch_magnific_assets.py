import io
import json
import hashlib
from pathlib import Path

from PIL import Image, ImageOps, ImageDraw
from playwright.sync_api import sync_playwright

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
manifest = []
thumbs = []


def save_webp(name, png_bytes, page_url, source_src, title):
    sha = hashlib.sha256(png_bytes).hexdigest()
    img = Image.open(io.BytesIO(png_bytes))
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
        "captured_from": source_src,
        "original_size": original_size,
        "saved_size": img.size,
        "sha256_capture": sha,
        "file": out_path.name,
        "title": title,
    })


with sync_playwright() as p:
    browser = p.chromium.launch(headless=True, args=["--disable-blink-features=AutomationControlled"])
    context = browser.new_context(
        viewport={"width": 1440, "height": 1100},
        user_agent="Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/151.0.0.0 Safari/537.36",
        locale="en-US",
    )
    page = context.new_page()

    for name, page_url in ASSETS.items():
        print(f"Opening {name}: {page_url}")
        response = page.goto(page_url, wait_until="domcontentloaded", timeout=90000)
        if response:
            print("HTTP", response.status)
        page.wait_for_timeout(3500)

        # Hide common consent/modal overlays when present.
        for selector in [
            'button:has-text("Accept")',
            'button:has-text("Accept all")',
            'button:has-text("I agree")',
            '[aria-label="Close"]',
        ]:
            try:
                loc = page.locator(selector).first
                if loc.is_visible(timeout=300):
                    loc.click(timeout=800)
            except Exception:
                pass

        images = page.locator("img")
        count = images.count()
        candidates = []
        for i in range(count):
            loc = images.nth(i)
            try:
                box = loc.bounding_box()
                if not box or box["width"] < 260 or box["height"] < 220:
                    continue
                meta = loc.evaluate("""el => ({src: el.currentSrc || el.src || '', alt: el.alt || '', nw: el.naturalWidth || 0, nh: el.naturalHeight || 0})""")
                src = meta.get("src", "")
                alt = meta.get("alt", "")
                if not src or src.startswith("data:"):
                    continue
                lower = src.lower()
                if any(x in lower for x in ["logo", "avatar", "icon", "banner"]):
                    continue
                score = box["width"] * box["height"] + meta.get("nw",0) * meta.get("nh",0) * 0.1
                if alt and name.split('-')[0] in alt.lower():
                    score *= 1.15
                candidates.append((score, i, src, alt, box))
            except Exception:
                continue

        if not candidates:
            # Capture page viewport as last-resort evidence rather than silently failing.
            shot = page.screenshot(full_page=False, type="png")
            save_webp(name, shot, page_url, "viewport-fallback", page.title())
            print("No large image found; used viewport fallback")
            continue

        candidates.sort(reverse=True, key=lambda x: x[0])
        _, idx, src, alt, box = candidates[0]
        target = images.nth(idx)
        try:
            target.scroll_into_view_if_needed(timeout=3000)
            page.wait_for_timeout(700)
            png = target.screenshot(type="png", timeout=10000)
        except Exception:
            png = page.screenshot(full_page=False, type="png")
            src = "viewport-fallback"
        print(f"Captured {name} from {src[:160]} alt={alt[:80]}")
        save_webp(name, png, page_url, src, page.title())

    browser.close()

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
print(f"Saved {len(manifest)} Magnific captures")
