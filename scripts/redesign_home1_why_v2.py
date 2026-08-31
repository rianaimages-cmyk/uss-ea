from pathlib import Path

path = Path('home1.html')
text = path.read_text(encoding='utf-8')

MARKER = 'HOME1 WHY MOSAIC V2'
CSS = r'''

    /* HOME1 WHY MOSAIC V2 */
    .home-one .why-section{
      padding:112px 0 120px !important;
      background:#fff !important;
      overflow:hidden;
    }
    .home-one .why-head{display:none !important;}

    .home-one .why-layout-new{
      width:min(1440px,calc(100% - 48px)) !important;
      margin:0 auto 64px !important;
      display:grid !important;
      grid-template-columns:1fr !important;
      gap:24px !important;
    }

    /* Horizontal editorial banner instead of left-side card */
    .home-one .why-visual-panel{
      position:relative !important;
      min-height:340px !important;
      width:100% !important;
      padding:36px 40px !important;
      border-radius:28px !important;
      overflow:hidden !important;
      background:
        linear-gradient(90deg,rgba(4,18,40,.92) 0%,rgba(4,18,40,.72) 36%,rgba(4,18,40,.18) 72%,rgba(4,18,40,.08) 100%),
        url('https://res.cloudinary.com/dwbjlidhm/image/upload/v1787988925/ChatGPT_Image_Aug_29_2026_10_28_06_AM_ylgat7.png') center 48%/cover no-repeat !important;
      box-shadow:0 26px 70px rgba(8,36,65,.13) !important;
    }
    .home-one .why-visual-panel::after{
      content:"";
      position:absolute;
      right:-70px;
      top:-80px;
      width:360px;
      height:360px;
      border-radius:50%;
      border:1px solid rgba(255,255,255,.15);
      box-shadow:0 0 0 50px rgba(255,255,255,.035),0 0 0 100px rgba(255,255,255,.02);
      pointer-events:none;
    }
    .home-one .why-visual-kicker{
      position:relative !important;
      z-index:3 !important;
      display:inline-flex !important;
      align-items:center !important;
      gap:10px !important;
      padding:8px 12px !important;
      border:1px solid rgba(255,255,255,.18) !important;
      border-radius:999px !important;
      background:rgba(255,255,255,.07) !important;
      color:#fff !important;
      font-size:11px !important;
      font-weight:700 !important;
      letter-spacing:.12em !important;
      backdrop-filter:blur(8px) !important;
    }
    .home-one .why-visual-index{
      position:absolute !important;
      z-index:1 !important;
      right:34px !important;
      top:24px !important;
      color:rgba(255,255,255,.12) !important;
      font-size:118px !important;
      line-height:.8 !important;
      font-weight:800 !important;
    }
    .home-one .why-visual-title{
      display:block !important;
      position:relative !important;
      z-index:3 !important;
      max-width:620px !important;
      margin:56px 0 0 !important;
      color:#fff !important;
      font-size:clamp(36px,3vw,50px) !important;
      line-height:1.02 !important;
      letter-spacing:-.04em !important;
      font-weight:800 !important;
      text-wrap:balance !important;
    }
    .home-one .why-visual-copy{
      display:block !important;
      position:relative !important;
      z-index:3 !important;
      left:auto !important;
      right:auto !important;
      bottom:auto !important;
      max-width:620px !important;
      margin:18px 0 0 !important;
      color:rgba(255,255,255,.75) !important;
      font-size:14px !important;
      line-height:1.7 !important;
    }

    /* Five-card capability row: same content, completely different interaction */
    .home-one .why-accordion{
      display:grid !important;
      grid-template-columns:repeat(5,minmax(0,1fr)) !important;
      gap:12px !important;
      align-items:start !important;
    }
    .home-one .why-item-new{
      position:relative !important;
      min-height:210px !important;
      overflow:hidden !important;
      border:1px solid #dfe7ef !important;
      border-radius:18px !important;
      background:#fff !important;
      box-shadow:0 12px 30px rgba(10,40,70,.055) !important;
      transition:transform .22s ease,border-color .22s ease,box-shadow .22s ease !important;
    }
    .home-one .why-item-new:hover,
    .home-one .why-item-new[open]{
      transform:translateY(-4px) !important;
      border-color:#bdd3e5 !important;
      box-shadow:0 18px 38px rgba(10,40,70,.10) !important;
    }
    .home-one .why-item-new::before{
      content:"";
      position:absolute;
      left:0;
      top:0;
      bottom:0;
      width:4px;
      background:linear-gradient(180deg,var(--uss-red),var(--uss-blue));
      opacity:.92;
    }
    .home-one .why-item-new summary{
      min-height:210px !important;
      display:flex !important;
      flex-direction:column !important;
      align-items:flex-start !important;
      justify-content:flex-start !important;
      gap:18px !important;
      padding:24px 22px 22px 26px !important;
      list-style:none !important;
      cursor:pointer !important;
    }
    .home-one .why-item-new summary::-webkit-details-marker{display:none !important;}
    .home-one .why-item-number{
      width:42px !important;
      height:42px !important;
      display:grid !important;
      place-items:center !important;
      border-radius:12px !important;
      background:#edf5fb !important;
      color:var(--uss-blue) !important;
      font-size:11px !important;
      font-weight:800 !important;
      letter-spacing:.04em !important;
      flex:0 0 auto !important;
    }
    .home-one .why-item-new[open] .why-item-number{
      background:var(--uss-blue) !important;
      color:#fff !important;
    }
    .home-one .why-item-title{
      max-width:190px !important;
      color:#111827 !important;
      font-size:16px !important;
      line-height:1.28 !important;
      font-weight:700 !important;
    }
    .home-one .why-item-toggle{
      position:absolute !important;
      right:18px !important;
      bottom:18px !important;
      width:32px !important;
      height:32px !important;
      display:grid !important;
      place-items:center !important;
      border-radius:50% !important;
      background:#f1f6fa !important;
      color:var(--uss-blue) !important;
      font-size:17px !important;
      transition:transform .2s ease,background .2s ease,color .2s ease !important;
    }
    .home-one .why-item-new[open] .why-item-toggle{
      transform:rotate(45deg) !important;
      background:var(--uss-red) !important;
      color:#fff !important;
    }
    .home-one .why-item-copy{
      margin:-72px 18px 18px 26px !important;
      padding:0 42px 0 0 !important;
      color:#687789 !important;
      font-size:12px !important;
      line-height:1.6 !important;
    }

    @media (max-width:1180px){
      .home-one .why-accordion{grid-template-columns:repeat(3,minmax(0,1fr)) !important;}
    }
    @media (max-width:820px){
      .home-one .why-layout-new{width:min(100% - 30px,1440px) !important;}
      .home-one .why-visual-panel{min-height:320px !important;padding:30px !important;}
      .home-one .why-accordion{grid-template-columns:repeat(2,minmax(0,1fr)) !important;}
    }
    @media (max-width:560px){
      .home-one .why-section{padding:78px 0 88px !important;}
      .home-one .why-layout-new{width:calc(100% - 24px) !important;gap:16px !important;}
      .home-one .why-visual-panel{min-height:300px !important;padding:24px !important;border-radius:22px !important;}
      .home-one .why-visual-title{margin-top:46px !important;font-size:32px !important;max-width:300px !important;}
      .home-one .why-visual-copy{font-size:12.5px !important;max-width:300px !important;}
      .home-one .why-visual-index{font-size:82px !important;right:18px !important;top:18px !important;}
      .home-one .why-accordion{grid-template-columns:1fr !important;gap:10px !important;}
      .home-one .why-item-new{min-height:auto !important;}
      .home-one .why-item-new summary{min-height:116px !important;padding:18px 18px 18px 22px !important;gap:14px !important;}
      .home-one .why-item-title{max-width:calc(100% - 44px) !important;font-size:15px !important;}
      .home-one .why-item-toggle{right:14px !important;bottom:14px !important;}
      .home-one .why-item-copy{margin:-42px 16px 16px 22px !important;padding-right:42px !important;}
    }
'''

if MARKER not in text:
    pos = text.rfind('</style>')
    if pos < 0:
        raise SystemExit('No </style> found in home1.html')
    text = text[:pos] + CSS + '\n  ' + text[pos:]
else:
    start = text.index('    /* HOME1 WHY MOSAIC V2 */')
    end = text.find('</style>', start)
    text = text[:start] + CSS + '\n  ' + text[end:]

path.write_text(text, encoding='utf-8')
