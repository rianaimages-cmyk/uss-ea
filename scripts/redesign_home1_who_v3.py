from pathlib import Path

path = Path('home1.html')
text = path.read_text(encoding='utf-8')

MARKER = 'HOME1 WHO LUXE SPLIT V3'
CSS = r'''

    /* HOME1 WHO LUXE SPLIT V3 */
    .home-one .who-section{
      position:relative;
      overflow:hidden;
      padding:118px 0;
      background:#06182d;
      color:#fff;
    }
    .home-one .who-section::before{
      content:"";
      position:absolute;
      inset:0;
      background:
        radial-gradient(circle at 12% 18%,rgba(20,86,141,.34),transparent 26%),
        radial-gradient(circle at 88% 78%,rgba(226,33,42,.13),transparent 24%),
        linear-gradient(120deg,#06182d 0%,#08213e 56%,#0b2d50 100%);
      pointer-events:none;
    }
    .home-one .who-section::after{
      content:"";
      position:absolute;
      width:520px;
      height:520px;
      left:-260px;
      bottom:-300px;
      border-radius:50%;
      border:1px solid rgba(255,255,255,.08);
      box-shadow:0 0 0 70px rgba(255,255,255,.025),0 0 0 140px rgba(255,255,255,.015);
      pointer-events:none;
    }

    .home-one .who-grid{
      position:relative;
      z-index:2;
      display:grid;
      grid-template-columns:minmax(0,1.05fr) minmax(420px,.95fr);
      gap:86px;
      align-items:center;
    }

    /* Put the copy first visually on desktop for a completely different composition. */
    .home-one .who-copy{
      grid-column:1;
      grid-row:1;
      padding:10px 0;
      max-width:760px;
    }
    .home-one .who-collage{
      grid-column:2;
      grid-row:1;
      position:relative;
      min-height:590px;
      overflow:visible;
      background:transparent;
      box-shadow:none;
      border-radius:0;
    }

    .home-one .who-copy .section-number{
      display:inline-flex;
      align-items:center;
      gap:11px;
      margin:0 0 24px;
      padding:8px 12px;
      border:1px solid rgba(255,255,255,.14);
      border-radius:999px;
      background:rgba(255,255,255,.055);
      color:#fff;
      font-size:11px;
      font-weight:900;
      letter-spacing:.14em;
      backdrop-filter:blur(8px);
    }
    .home-one .who-copy .section-number::before{
      content:"";
      width:7px;
      height:7px;
      border-radius:50%;
      background:var(--uss-red);
      box-shadow:0 0 0 5px rgba(226,33,42,.13);
    }

    .home-one .who-copy h2{
      max-width:760px;
      margin:0 0 30px;
      color:#fff;
      font-size:clamp(44px,4vw,68px);
      line-height:.98;
      letter-spacing:-.052em;
      font-weight:900;
      text-wrap:balance;
    }
    .home-one .who-copy h2::first-line{color:#fff;}

    .home-one .who-copy p{
      max-width:700px;
      margin:0;
      color:rgba(255,255,255,.70);
      font-size:15px;
      line-height:1.82;
    }
    .home-one .who-copy p + p{margin-top:17px;}
    .home-one .who-copy p a{
      color:#fff!important;
      font-weight:900;
      text-decoration:none!important;
      border-bottom:1px solid rgba(255,255,255,.48);
    }
    .home-one .who-simple-cta{margin-top:32px;}
    .home-one .who-cta-button{
      min-height:56px;
      padding:0 24px;
      border-radius:999px;
      background:#fff;
      color:#0b2d50;
      box-shadow:0 16px 38px rgba(0,0,0,.22);
      font-size:14px;
      font-weight:900;
      transition:transform .2s ease,box-shadow .2s ease,color .2s ease;
    }
    .home-one .who-cta-button:hover{
      transform:translateY(-2px);
      background:#fff;
      color:var(--uss-red);
      box-shadow:0 22px 46px rgba(0,0,0,.28);
    }

    /* New vertical gallery on the right */
    .home-one .who-collage::before{
      content:"";
      position:absolute;
      z-index:0;
      top:26px;
      right:18px;
      width:78%;
      height:88%;
      border-radius:34px;
      border:1px solid rgba(255,255,255,.13);
      background:rgba(255,255,255,.045);
      backdrop-filter:blur(14px);
      box-shadow:0 26px 70px rgba(0,0,0,.24);
    }
    .home-one .who-image{
      position:absolute;
      overflow:hidden;
      border:1px solid rgba(255,255,255,.22);
      background-size:cover;
      background-position:center;
      box-shadow:0 24px 58px rgba(0,0,0,.28);
    }
    .home-one .who-image-main{
      z-index:2;
      left:0;
      top:0;
      width:72%;
      height:72%;
      inset:auto;
      border-radius:28px;
      transform:rotate(-2.5deg);
    }
    .home-one .who-image-overlap{
      z-index:3;
      right:0;
      bottom:0;
      width:55%;
      height:48%;
      inset:auto;
      border:7px solid #0a2747;
      border-radius:24px;
      transform:rotate(2.2deg);
    }
    .home-one .who-collage::after{
      content:"";
      position:absolute;
      z-index:5;
      left:44px;
      bottom:28px;
      width:106px;
      height:8px;
      border-radius:999px;
      background:linear-gradient(90deg,var(--uss-red) 0 34%,#fff 34% 64%,var(--uss-blue) 64% 100%);
      box-shadow:0 8px 24px rgba(0,0,0,.22);
    }

    @media (max-width:1080px){
      .home-one .who-grid{grid-template-columns:1fr;gap:50px;}
      .home-one .who-copy,.home-one .who-collage{grid-column:1;}
      .home-one .who-copy{grid-row:1;max-width:880px;}
      .home-one .who-collage{grid-row:2;min-height:520px;max-width:760px;width:100%;}
    }
    @media (max-width:680px){
      .home-one .who-section{padding:78px 0;}
      .home-one .who-grid{gap:36px;}
      .home-one .who-copy h2{font-size:clamp(38px,11vw,52px);}
      .home-one .who-copy p{font-size:14px;line-height:1.72;}
      .home-one .who-cta-button{width:100%;justify-content:center;}
      .home-one .who-collage{min-height:400px;}
      .home-one .who-collage::before{top:22px;right:0;width:82%;height:88%;border-radius:24px;}
      .home-one .who-image-main{width:78%;height:70%;border-radius:20px;transform:rotate(-1.5deg);}
      .home-one .who-image-overlap{width:58%;height:46%;border-width:5px;border-radius:18px;}
      .home-one .who-collage::after{left:20px;bottom:10px;width:78px;height:6px;}
    }
'''

if MARKER not in text:
    pos = text.rfind('</style>')
    if pos < 0:
        raise SystemExit('No </style> found')
    text = text[:pos] + CSS + '\n  ' + text[pos:]
else:
    start = text.index('    /* HOME1 WHO LUXE SPLIT V3 */')
    end = text.find('</style>', start)
    text = text[:start] + CSS + '\n  ' + text[end:]

path.write_text(text, encoding='utf-8')
