from pathlib import Path
import re

ICONS = {
    'Hospitality': 'https://res.cloudinary.com/dwbjlidhm/image/upload/e_colorize:100,co_rgb:14568D/v1787905192/Hospitality_rtttuv.svg',
    'Commercial office buildings': 'https://res.cloudinary.com/dwbjlidhm/image/upload/e_colorize:100,co_rgb:14568D/v1787905558/Commercial_office_buildings_dehf58.svg',
    'Residential': 'https://res.cloudinary.com/dwbjlidhm/image/upload/e_colorize:100,co_rgb:14568D/v1787905192/Residential_gympvb.svg',
    'Banking & Insurance': 'https://res.cloudinary.com/dwbjlidhm/image/upload/e_colorize:100,co_rgb:14568D/v1787905193/Banking_Insurance_o5eyhq.svg',
    'Healthcare': 'https://res.cloudinary.com/dwbjlidhm/image/upload/e_colorize:100,co_rgb:14568D/v1787905193/Healthcare_fmtdga.svg',
    'Malls & Retail': 'https://res.cloudinary.com/dwbjlidhm/image/upload/e_colorize:100,co_rgb:14568D/v1787905194/Malls_Retail_bf4xzp.svg',
    'Government & NGOs': 'https://res.cloudinary.com/dwbjlidhm/image/upload/e_colorize:100,co_rgb:14568D/v1787905194/Government_NGOs_t4telo.svg',
    'Automotive': 'https://res.cloudinary.com/dwbjlidhm/image/upload/e_colorize:100,co_rgb:14568D/v1787905192/Automotive_tzmzop.svg',
    'Energy': 'https://res.cloudinary.com/dwbjlidhm/image/upload/e_colorize:100,co_rgb:14568D/v1787905192/Energy_2_lflpgc.svg',
}

MARKER='CLOUDINARY ENVIRONMENT ICONS'
CSS=r'''

    /* CLOUDINARY ENVIRONMENT ICONS */
    .environments-section .environment-icon{
      width:42px !important;
      height:42px !important;
      padding:9px !important;
      background:#fff !important;
      border:1px solid rgba(255,255,255,.42) !important;
      box-shadow:0 8px 20px rgba(0,0,0,.12) !important;
    }
    .environments-section .environment-icon img{
      display:block;
      width:100%;
      height:100%;
      object-fit:contain;
    }
    .environments-section .environment-item::after{
      background:var(--uss-red) !important;
    }
'''

for filename in ('index.html','home1.html'):
    p=Path(filename)
    text=p.read_text(encoding='utf-8')

    for title, url in ICONS.items():
        pattern = re.compile(
            r'(<article class="environment-item" role="listitem"><div class="environment-icon">).*?(</div><h3>'+re.escape(title)+r'</h3></article>)',
            re.S
        )
        replacement = r'\1<img alt="" aria-hidden="true" src="' + url + r'"/>\2'
        text, count = pattern.subn(replacement, text, count=1)
        if count == 0:
            raise SystemExit(f'Could not find environment item: {title} in {filename}')

    if MARKER not in text:
        pos=text.rfind('</style>')
        if pos<0:
            raise SystemExit(f'No </style> found in {filename}')
        text=text[:pos]+CSS+'\n  '+text[pos:]

    p.write_text(text,encoding='utf-8')
