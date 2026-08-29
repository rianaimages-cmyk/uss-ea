from pathlib import Path

REPLACEMENTS = {
    "assets/placeholders/smart-surveillance.svg": "https://res.cloudinary.com/dwbjlidhm/image/upload/v1787837185/cctv_camera_dcsacm.png",
    "assets/placeholders/pedestrian-entrance-control.svg": "https://res.cloudinary.com/dwbjlidhm/image/upload/v1787837185/Pedestrian_entrance_control_xtpu7r.png",
    "assets/placeholders/scanners-and-detectors.svg": "https://res.cloudinary.com/dwbjlidhm/image/upload/v1787919070/scanners_and_detectors_swahsx.png",
    "assets/placeholders/building-management-system.svg": "https://res.cloudinary.com/dwbjlidhm/image/upload/v1787837185/bms_gi6rcg.png",
    "assets/placeholders/visitor-management-system.svg": "https://res.cloudinary.com/dwbjlidhm/image/upload/v1787990091/visitor_managment_system_lgxgyt.png",
    "assets/placeholders/public-address-voice-alarm.svg": "https://res.cloudinary.com/dwbjlidhm/image/upload/v1787990092/Public_address_system_uj1jk4.png",
    "assets/placeholders/fire-detection-system.svg": "https://res.cloudinary.com/dwbjlidhm/image/upload/v1787990093/fire_dection_system_wllhid.png",
}

for filename in ("index.html", "home1.html"):
    path = Path(filename)
    text = path.read_text(encoding="utf-8")
    for old, new in REPLACEMENTS.items():
        if old in text:
            text = text.replace(old, new)
        elif new not in text:
            raise SystemExit(f"Neither old nor new offering image reference found in {filename}: {old}")
    path.write_text(text, encoding="utf-8")
