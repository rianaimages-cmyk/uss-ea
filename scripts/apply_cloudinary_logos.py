from pathlib import Path
import re

REGULAR='https://res.cloudinary.com/dwbjlidhm/image/upload/v1787903501/RIANA_fiunlc.png'
WHITE='https://res.cloudinary.com/dwbjlidhm/image/upload/v1787903501/USS_WHITE_LOGO_ejsabt.png'

for filename in ('index.html','home1.html'):
    p=Path(filename)
    text=p.read_text(encoding='utf-8')

    # Header / navigation logo -> regular USS logo
    text=re.sub(
        r'(<a class="brand"[^>]*>\s*<img[^>]*?src=")[^"]+("[^>]*>)',
        lambda m: m.group(1)+REGULAR+m.group(2),
        text,
        count=1,
        flags=re.S,
    )

    # Contact strip logo -> white USS logo
    text=re.sub(
        r'(<div class="footer-contact-brand">\s*<img[^>]*?src=")[^"]+("[^>]*>)',
        lambda m: m.group(1)+WHITE+m.group(2),
        text,
        count=1,
        flags=re.S,
    )

    # Main dark footer logo -> white USS logo
    text=re.sub(
        r'(<div class="footer-brand">\s*<img[^>]*?src=")[^"]+("[^>]*>)',
        lambda m: m.group(1)+WHITE+m.group(2),
        text,
        count=1,
        flags=re.S,
    )

    p.write_text(text,encoding='utf-8')
