from pathlib import Path

# Existing offering-image replacements.
REPLACEMENTS = {
    "assets/placeholders/smart-surveillance.svg": "https://res.cloudinary.com/dwbjlidhm/image/upload/v1787837185/cctv_camera_dcsacm.png",
    "assets/placeholders/pedestrian-entrance-control.svg": "https://res.cloudinary.com/dwbjlidhm/image/upload/v1787837185/Pedestrian_entrance_control_xtpu7r.png",
    "assets/placeholders/scanners-and-detectors.svg": "https://res.cloudinary.com/dwbjlidhm/image/upload/v1787919070/scanners_and_detectors_swahsx.png",
    "assets/placeholders/building-management-system.svg": "https://res.cloudinary.com/dwbjlidhm/image/upload/v1787837185/bms_gi6rcg.png",
    "assets/placeholders/visitor-management-system.svg": "https://res.cloudinary.com/dwbjlidhm/image/upload/v1787990091/visitor_managment_system_lgxgyt.png",
    "assets/placeholders/public-address-voice-alarm.svg": "https://res.cloudinary.com/dwbjlidhm/image/upload/v1787990092/Public_address_system_uj1jk4.png",
    "assets/placeholders/fire-detection-system.svg": "https://res.cloudinary.com/dwbjlidhm/image/upload/v1787990093/fire_dection_system_wllhid.png",
}

# New images supplied for the remaining offering cards. Multiple candidate placeholder
# names are supported so this remains compatible with the earlier site builds.
NEW_OFFERING_IMAGES = [
    (
        "https://res.cloudinary.com/dwbjlidhm/image/upload/v1788179234/parking_guideance_system_cajnhx.png",
        [
            "assets/placeholders/parking-guidance-system.svg",
            "assets/placeholders/parking-guidance-management.svg",
            "assets/placeholders/parking-guidance.svg",
        ],
    ),
    (
        "https://res.cloudinary.com/dwbjlidhm/image/upload/v1788179228/ict_infrastructure_zpz22q.png",
        [
            "assets/placeholders/ict-infrastructure.svg",
            "assets/placeholders/ict-infrastructure-system.svg",
        ],
    ),
    (
        "https://res.cloudinary.com/dwbjlidhm/image/upload/v1788179228/paid_parking_management_qo4kib.png",
        [
            "assets/placeholders/paid-parking-management-system.svg",
            "assets/placeholders/paid-parking-management.svg",
            "assets/placeholders/parking-management-system.svg",
        ],
    ),
    (
        "https://res.cloudinary.com/dwbjlidhm/image/upload/v1788179226/video_intercom_solutions_ewkxr5.png",
        [
            "assets/placeholders/video-intercom-system.svg",
            "assets/placeholders/video-intercom.svg",
        ],
    ),
    (
        "https://res.cloudinary.com/dwbjlidhm/image/upload/v1788179226/meeting_room_booking_solutions_u5bkly.png",
        [
            "assets/placeholders/meeting-room-booking-system.svg",
            "assets/placeholders/meeting-room-booking.svg",
        ],
    ),
    (
        "https://res.cloudinary.com/dwbjlidhm/image/upload/v1788179224/ip_telephone_gjbkvy.png",
        [
            "assets/placeholders/ip-telephone.svg",
            "assets/placeholders/ip-telephone-system.svg",
        ],
    ),
    (
        "https://res.cloudinary.com/dwbjlidhm/image/upload/v1788180534/vehicular_entrance_control_pngcbc.png",
        [
            "assets/placeholders/vehicular-entrance-control.svg",
            "assets/placeholders/vehicle-entrance-control.svg",
            "assets/placeholders/vehicular-access-control.svg",
        ],
    ),
    (
        "https://res.cloudinary.com/dwbjlidhm/image/upload/v1788179915/board_room_solutions_z6qncu.png",
        [
            "assets/placeholders/boardroom-solutions.svg",
            "assets/placeholders/board-room-solutions.svg",
            "assets/placeholders/boardroom.svg",
        ],
    ),
    (
        "https://res.cloudinary.com/dwbjlidhm/image/upload/v1788179915/perimeter_detection_system_zbhxdt.png",
        [
            "assets/placeholders/perimeter-detection-system.svg",
            "assets/placeholders/perimeter-security.svg",
            "assets/placeholders/perimeter-security-system.svg",
        ],
    ),
]

for filename in ("index.html", "home1.html"):
    path = Path(filename)
    text = path.read_text(encoding="utf-8")

    for old, new in REPLACEMENTS.items():
        if old in text:
            text = text.replace(old, new)

    for new_url, candidates in NEW_OFFERING_IMAGES:
        if new_url in text:
            continue
        for old in candidates:
            if old in text:
                text = text.replace(old, new_url)
                break

    path.write_text(text, encoding="utf-8")
