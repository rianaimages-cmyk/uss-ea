from pathlib import Path
import re

ICONS = [
    ('Hospitality','https://res.cloudinary.com/dwbjlidhm/image/upload/e_colorize:100,co_rgb:14568D/v1787905192/Hospitality_rtttuv.svg'),
    ('Commercial office buildings','https://res.cloudinary.com/dwbjlidhm/image/upload/e_colorize:100,co_rgb:14568D/v1787905558/Commercial_office_buildings_dehf58.svg'),
    ('Residential','https://res.cloudinary.com/dwbjlidhm/image/upload/e_colorize:100,co_rgb:14568D/v1787905192/Residential_gympvb.svg'),
    ('Banking &amp; Insurance','https://res.cloudinary.com/dwbjlidhm/image/upload/e_colorize:100,co_rgb:14568D/v1787905193/Banking_Insurance_o5eyhq.svg'),
    ('Healthcare','https://res.cloudinary.com/dwbjlidhm/image/upload/e_colorize:100,co_rgb:14568D/v1787905193/Healthcare_fmtdga.svg'),
    ('Malls &amp; Retail','https://res.cloudinary.com/dwbjlidhm/image/upload/e_colorize:100,co_rgb:14568D/v1787905194/Malls_Retail_bf4xzp.svg'),
    ('Government &amp; NGOs','https://res.cloudinary.com/dwbjlidhm/image/upload/e_colorize:100,co_rgb:14568D/v1787905194/Government_NGOs_t4telo.svg'),
    ('Automotive','https://res.cloudinary.com/dwbjlidhm/image/upload/e_colorize:100,co_rgb:14568D/v1787905192/Automotive_tzmzop.svg'),
    ('Energy','https://res.cloudinary.com/dwbjlidhm/image/upload/e_colorize:100,co_rgb:14568D/v1787905192/Energy_2_lflpgc.svg'),
]

ENV_SECTION = '''<section aria-labelledby="environments-title" class="environments-section" id="environments">
<div class="shell">
<div class="section-centered-head">
<div class="section-number">07 — ENVIRONMENTS WE SUPPORT</div>
<h2 id="environments-title">Security designed around different operating environments</h2>
<p>USS solutions support a broad range of industries, including:</p>
</div>
<div class="environment-grid" role="list">{cards}</div>
</div>
</section>'''

cards=''.join(
    f'<article class="environment-item" role="listitem"><div class="environment-icon"><img alt="" aria-hidden="true" src="{url}"/></div><h3>{title}</h3></article>'
    for title,url in ICONS
)
ENV_SECTION=ENV_SECTION.format(cards=cards)

CSS_MARK='ENV FOOTER REPAIR 2026-08-28'
CSS='''

    /* ENV FOOTER REPAIR 2026-08-28 */
    .environments-section .environment-grid{
      display:grid !important;
      grid-template-columns:repeat(9,minmax(0,1fr)) !important;
      gap:12px !important;
      overflow-x:auto !important;
      padding:4px 0 14px !important;
    }
    .environments-section .environment-item{
      min-width:118px !important;
    }
    .environments-section .environment-icon{
      width:46px !important;
      height:46px !important;
      padding:9px !important;
      background:#fff !important;
      border:1px solid rgba(20,86,141,.14) !important;
      border-radius:13px !important;
    }
    .environments-section .environment-icon img{
      width:100% !important;
      height:100% !important;
      display:block !important;
      object-fit:contain !important;
    }
    .environments-section .environment-item::after{background:var(--uss-red) !important;}
    @media (max-width:1100px){
      .environments-section .environment-grid{grid-template-columns:repeat(9,132px) !important;}
    }
'''

for filename in ('index.html','home1.html'):
    p=Path(filename)
    text=p.read_text(encoding='utf-8')

    # Replace the whole environments section in one operation so all 9 cards survive.
    text, n = re.subn(
        r'<section aria-labelledby="environments-title" class="environments-section" id="environments">.*?</section>\s*(?=<section aria-labelledby="case-studies-title")',
        ENV_SECTION+'\n', text, count=1, flags=re.S
    )
    if n != 1:
        raise SystemExit(f'Could not replace environments section in {filename}')

    # Keep only the logo in the top contact banner; remove the duplicate lower footer logo.
    text, n2 = re.subn(
        r'(<div class="footer-brand">\s*)<img[^>]*>\s*',
        r'\1', text, count=1, flags=re.S
    )
    if n2 != 1 and '<div class="footer-brand">' in text and '<div class="footer-brand">\n<p>' not in text:
        raise SystemExit(f'Could not remove duplicate footer logo in {filename}')

    if CSS_MARK not in text:
        pos=text.rfind('</style>')
        if pos < 0:
            raise SystemExit(f'No </style> in {filename}')
        text=text[:pos]+CSS+'\n  '+text[pos:]

    p.write_text(text,encoding='utf-8')
