from pathlib import Path

REPLACEMENTS = {
    "assets/placeholders/smart-surveillance.svg": "https://res.cloudinary.com/dwbjlidhm/image/upload/v1787837185/cctv_camera_dcsacm.png",
    "assets/placeholders/pedestrian-entrance-control.svg": "https://res.cloudinary.com/dwbjlidhm/image/upload/v1787837185/Pedestrian_entrance_control_xtpu7r.png",
    "assets/placeholders/scanners-and-detectors.svg": "https://res.cloudinary.com/dwbjlidhm/image/upload/v1787919070/scanners_and_detectors_swahsx.png",
    "assets/placeholders/building-management-system.svg": "https://res.cloudinary.com/dwbjlidhm/image/upload/v1787837185/bms_gi6rcg.png",
}

for filename in ("index.html", "home1.html"):
    path = Path(filename)
    text = path.read_text(encoding="utf-8")
    for old, new in REPLACEMENTS.items():
        if old not in text:
            raise SystemExit(f"Expected offering image reference not found in {filename}: {old}")
        text = text.replace(old, new)
    path.write_text(text, encoding="utf-8")
