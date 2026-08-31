from pathlib import Path

path = Path('home1.html')
text = path.read_text(encoding='utf-8')

MARKER = 'HOME1 WHY FEATURE GRID V4'
WHY_IMAGE = 'https://res.cloudinary.com/dwbjlidhm/image/upload/v1787988925/ChatGPT_Image_Aug_29_2026_10_28_06_AM_ylgat7.png'

CSS = rf'''

    /* HOME1 WHY FEATURE GRID V4 */
    .home-one .why-section{{
      padding:108px 0 118px !important;
      background:#f6f8fb !important;
      overflow:hidden !important;
    }}
    .home-one .why-head{{display:none !important;}}
    .home-one .why-layout-new{{
      display:grid !important;
      grid-template-columns:repeat(12,minmax(0,1fr)) !important;
      gap:18px !important;
      margin-bottom:64px !important;
      align-items:stretch !important;
    }}

    /* Full-width image banner instead of a left-side image card */
    .home-one .why-visual-panel{{
      grid-column:1 / -1 !important;
      min-height:360px !important;
      position:relative !important;
      overflow:hidden !important;
      padding:38px 40px !important;
      border-radius:28px !important;
      background:
        linear-gradient(90deg,rgba(4,19,38,.91) 0%,rgba(4,19,38,.72) 42%,rgba(4,19,38,.18) 78%,rgba(4,19,38,.08) 100%),
        url('{WHY_IMAGE}') center 52%/cover no-repeat !important;
      box-shadow:0 24px 58px rgba(8,35,64,.14) !important;
    }}
    .home-one .why-visual-panel::before{{
      content:"" !important;
      position:absolute !important;
      inset:auto 0 0 0 !important;
      height:5px !important;
      background:linear-gradient(90deg,var(--uss-red) 0 20%,var(--uss-blue) 20% 100%) !important;
      display:block !important;
    }}
    .home-one .why-visual-kicker{{
      display:inline-flex !important;
      align-items:center !important;
      gap:9px !important;
      padding:8px 12px !important;
      border-radius:999px !important;
      background:rgba(255,255,255,.10) !important;
      color:#fff !important;
      border:1px solid rgba(255,255,255,.15) !important;
      backdrop-filter:blur(8px) !important;
      font-size:11px !important;
      font-weight:700 !important;
      letter-spacing:.12em !important;
    }}
    .home-one .why-visual-kicker::before{{
      content:"" !important;
      width:7px !important;
      height:7px !important;
      border-radius:50% !important;
      background:var(--uss-red) !important;
      box-shadow:0 0 0 5px rgba(226,33,42,.14) !important;
    }}
    .home-one .why-visual-index{{
      right:28px !important;
      top:22px !important;
      color:rgba(255,255,255,.08) !important;
      font-size:110px !important;
      line-height:.8 !important;
      font-weight:800 !important;
    }}
    .home-one .why-visual-title{{
      display:block !important;
      position:relative !important;
      z-index:2 !important;
      max-width:680px !important;
      margin:56px 0 0 !important;
      color:#fff !important;
      font-size:clamp(38px,3.4vw,56px) !important;
      line-height:1.02 !important;
      font-weight:800 !important;
      letter-spacing:-.04em !important;
      text-wrap:balance !important;
      text-shadow:0 3px 18px rgba(0,0,0,.28) !important;
    }}
    .home-one .why-visual-copy{{
      display:block !important;
      position:relative !important;
      left:auto !important;
      right:auto !important;
      bottom:auto !important;
      z-index:2 !important;
      max-width:680px !important;
      margin:22px 0 0 !important;
      color:rgba(255,255,255,.80) !important;
      font-size:14px !important;
      line-height:1.75 !important;
      text-shadow:none !important;
    }}

    /* New capability-card grid */
    .home-one .why-accordion{{
      grid-column:1 / -1 !important;
      display:grid !important;
      grid-template-columns:repeat(3,minmax(0,1fr)) !important;
      gap:14px !important;
    }}
    .home-one .why-item-new{{
      position:relative !important;
      min-height:190px !important;
      overflow:hidden !important;
      border:1px solid #dce6ef !important;
      border-radius:20px !important;
      background:#fff !important;
      box-shadow:none !important;
      transition:transform .22s ease,border-color .22s ease,box-shadow .22s ease !important;
    }}
    .home-one .why-item-new:hover{{
      transform:translateY(-4px) !important;
      border-color:#bdd2e4 !important;
      box-shadow:0 18px 36px rgba(13,48,81,.08) !important;
    }}
    .home-one .why-item-new[open]{{
      border-color:#a9c8df !important;
      box-shadow:0 18px 36px rgba(13,48,81,.09) !important;
    }}
    .home-one .why-item-new summary{{
      min-height:auto !important;
      display:grid !important;
      grid-template-columns:1fr 36px !important;
      gap:14px !important;
      align-items:start !important;
      padding:24px 22px 18px !important;
      list-style:none !important;
    }}
    .home-one .why-item-number{{
      position:absolute !important;
      left:22px !important;
      bottom:18px !important;
      width:auto !important;
      height:auto !important;
      display:block !important;
      border-radius:0 !important;
      background:transparent !important;
      color:#9cb0c3 !important;
      font-size:42px !important;
      line-height:1 !important;
      font-weight:700 !important;
      letter-spacing:-.06em !important;
    }}
    .home-one .why-item-new[open] .why-item-number{{
      background:transparent !important;
      color:rgba(20,86,141,.22) !important;
    }}
    .home-one .why-item-title{{
      grid-column:1 !important;
      max-width:88% !important;
      color:#111a28 !important;
      font-size:18px !important;
      line-height:1.25 !important;
      font-weight:700 !important;
    }}
    .home-one .why-item-toggle{{
      grid-column:2 !important;
      grid-row:1 !important;
      width:34px !important;
      height:34px !important;
      justify-self:end !important;
      border-radius:50% !important;
      background:#eff5f9 !important;
      color:var(--uss-blue) !important;
      font-size:18px !important;
      font-weight:500 !important;
      transform:none !important;
    }}
    .home-one .why-item-new[open] .why-item-toggle{{
      background:var(--uss-red) !important;
      color:#fff !important;
      transform:rotate(45deg) !important;
    }}
    .home-one .why-item-copy{{
      position:relative !important;
      z-index:2 !important;
      padding:0 22px 74px !important;
      color:#657487 !important;
      font-size:13px !important;
      line-height:1.7 !important;
    }}

    /* Make first two cards span more width for an editorial rhythm */
    .home-one .why-item-new:nth-child(1){{grid-column:span 2 !important;}}
    .home-one .why-item-new:nth-child(2){{grid-column:span 1 !important;}}
    .home-one .why-item-new:nth-child(3),
    .home-one .why-item-new:nth-child(4),
    .home-one .why-item-new:nth-child(5){{grid-column:span 1 !important;}}

    @media (max-width:1000px){{
      .home-one .why-accordion{{grid-template-columns:repeat(2,minmax(0,1fr)) !important;}}
      .home-one .why-item-new:nth-child(1){{grid-column:span 2 !important;}}
      .home-one .why-item-new:nth-child(n+2){{grid-column:span 1 !important;}}
    }}
    @media (max-width:680px){{
      .home-one .why-section{{padding:76px 0 84px !important;}}
      .home-one .why-layout-new{{gap:12px !important;margin-bottom:44px !important;}}
      .home-one .why-visual-panel{{min-height:320px !important;padding:24px 20px !important;border-radius:22px !important;}}
      .home-one .why-visual-title{{margin-top:44px !important;font-size:clamp(32px,9vw,42px) !important;}}
      .home-one .why-visual-copy{{font-size:13px !important;line-height:1.65 !important;}}
      .home-one .why-accordion{{grid-template-columns:1fr !important;gap:10px !important;}}
      .home-one .why-item-new:nth-child(n){{grid-column:1 !important;}}
      .home-one .why-item-new{{min-height:170px !important;border-radius:16px !important;}}
      .home-one .why-item-new summary{{padding:20px 18px 16px !important;}}
      .home-one .why-item-number{{left:18px !important;bottom:16px !important;font-size:36px !important;}}
      .home-one .why-item-copy{{padding:0 18px 66px !important;}}
    }}
'''

if MARKER not in text:
    pos = text.rfind('</style>')
    if pos < 0:
        raise SystemExit('No </style> found in home1.html')
    text = text[:pos] + CSS + '\n  ' + text[pos:]
else:
    start = text.index('    /* HOME1 WHY FEATURE GRID V4 */')
    end = text.find('</style>', start)
    text = text[:start] + CSS + '\n  ' + text[end:]

path.write_text(text, encoding='utf-8')
