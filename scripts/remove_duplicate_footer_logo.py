from pathlib import Path
import re

for filename in ('index.html','home1.html'):
    p=Path(filename)
    text=p.read_text(encoding='utf-8')

    # Keep the USS logo in the contact banner and remove the duplicate logo
    # from the lower footer brand block.
    text=re.sub(
        r'(<div class="footer-brand">\s*)<img[^>]*>\s*',
        r'\1',
        text,
        count=1,
        flags=re.S,
    )

    p.write_text(text,encoding='utf-8')
