from pathlib import Path

path = Path('home1.html')
text = path.read_text(encoding='utf-8')

MARKER = 'HOME1 WHO SECTION REDESIGN V2'
CSS = r'''

    /* HOME1 WHO SECTION REDESIGN V2 */
    .home-one .who-section{
      position:relative;
      overflow:hidden;
      padding:120px 0;
      background:
        radial-gradient(circle at 88% 12%,rgba(20,86,141,.08),transparent 23%),
        linear-gradient(180deg,#f7fafe 0%,#ffffff 100%);
    }
    .home-one .who-section::before{
      content:"";
      position:absolute;
      width:520px;
      height:520px;
      right:-280px;
      top:-250px;
      border:70px solid rgba(20,86,141,.045);
      border-radius:50%;
      pointer-events:none;
    }
    .home-one .who-grid{
      position:relative;
      z-index:2;
      display:grid;
      grid-template-columns:minmax(0,.92fr) minmax(0,1.08fr);
      gap:88px;
      align-items:center;
    }

    .home-one .who-collage{
      position:relative;
      min-height:580px;
      border-radius:34px;
      overflow:visible;
      background:transparent;
      box-shadow:none;
    }
    .home-one .who-collage::before{
      content:"";
      position:absolute;
      inset:48px 42px 26px 0;
      border-radius:30px;
      background:#eaf2f8;
      box-shadow:0 28px 70px rgba(11,42,72,.10);
    }
    .home-one .who-image{
      box-shadow:none;
      overflow:hidden;
      background-position:center;
      background-size:cover;
      background-repeat:no-repeat;
    }
    .home-one .who-image-main{
      position:absolute;
      z-index:2;
      left:0;
      top:0;
      width:76%;
      height:76%;
      inset:auto;
      border-radius:28px;
      box-shadow:0 26px 58px rgba(6,26,49,.18);
    }
    .home-one .who-image-overlap{
      position:absolute;
      z-index:3;
      right:0;
      bottom:0;
      width:48%;
      height:46%;
      inset:auto;
      border:7px solid #fff;
      border-radius:24px;
      box-shadow:0 22px 52px rgba(6,26,49,.20);
    }
    .home-one .who-collage::after{
      content:"";
      position:absolute;
      z-index:4;
      left:34px;
      bottom:4px;
      width:92px;
      height:8px;
      border-radius:999px;
      background:linear-gradient(90deg,var(--uss-red) 0 38%,var(--uss-blue) 38% 100%);
    }

    .home-one .who-copy{
      padding:12px 0 10px;
    }
    .home-one .who-copy .section-number{
      display:inline-flex;
      align-items:center;
      gap:12px;
      margin-bottom:22px;
      color:var(--uss-red);
      font-size:12px;
      font-weight:900;
      letter-spacing:.14em;
    }
    .home-one .who-copy .section-number::before{
      content:"";
      width:34px;
      height:3px;
      border-radius:999px;
      background:var(--uss-red);
    }
    .home-one .who-copy h2{
      max-width:760px;
      margin:0 0 28px;
      color:#0d1727;
      font-size:clamp(42px,4.15vw,70px);
      line-height:.98;
      letter-spacing:-.052em;
      font-weight:900;
      text-wrap:balance;
    }
    .home-one .who-copy h2::first-line{
      color:var(--uss-blue);
    }
    .home-one .who-copy p{
      max-width:760px;
      color:#637286;
      font-size:15px;
      line-height:1.82;
    }
    .home-one .who-copy p + p{margin-top:16px;}
    .home-one .who-copy a:not(.who-cta-button){
      color:var(--uss-blue);
      font-weight:800;
      text-decoration:underline;
      text-underline-offset:3px;
    }
    .home-one .who-simple-cta{
      margin-top:28px;
    }
    .home-one .who-cta-button{
      min-height:54px;
      padding:0 24px;
      border-radius:12px;
      background:var(--uss-blue);
      box-shadow:0 14px 32px rgba(20,86,141,.20);
      transition:transform .2s ease,box-shadow .2s ease,background .2s ease;
    }
    .home-one .who-cta-button:hover{
      transform:translateY(-2px);
      background:var(--uss-blue-dark);
      box-shadow:0 18px 38px rgba(20,86,141,.26);
    }

    @media (max-width:1050px){
      .home-one .who-grid{grid-template-columns:1fr;gap:52px;}
      .home-one .who-collage{min-height:500px;max-width:720px;}
      .home-one .who-copy{max-width:820px;}
    }
    @media (max-width:680px){
      .home-one .who-section{padding:76px 0;}
      .home-one .who-grid{gap:34px;}
      .home-one .who-collage{min-height:390px;}
      .home-one .who-collage::before{inset:32px 18px 20px 0;border-radius:22px;}
      .home-one .who-image-main{width:82%;height:74%;border-radius:20px;}
      .home-one .who-image-overlap{width:54%;height:44%;border-width:5px;border-radius:18px;}
      .home-one .who-collage::after{left:18px;width:72px;height:6px;}
      .home-one .who-copy h2{font-size:clamp(36px,11vw,52px);line-height:1;}
      .home-one .who-copy p{font-size:14px;line-height:1.72;}
      .home-one .who-cta-button{width:100%;justify-content:center;}
    }
'''

if MARKER not in text:
    pos = text.rfind('</style>')
    if pos < 0:
        raise SystemExit('No </style> found')
    text = text[:pos] + CSS + '\n  ' + text[pos:]
else:
    start = text.index('    /* HOME1 WHO SECTION REDESIGN V2 */')
    end = text.find('</style>', start)
    text = text[:start] + CSS + '\n  ' + text[end:]

path.write_text(text, encoding='utf-8')
