from pathlib import Path

path = Path('home1.html')
text = path.read_text(encoding='utf-8')

MARKER = 'HOME1 OFFERINGS FULL WIDTH V2'
CSS = r'''

    /* HOME1 OFFERINGS FULL WIDTH V2 */
    .home-one .offerings-section{
      padding:112px 0 124px !important;
      background:#f7f9fc !important;
      overflow:hidden;
    }
    .home-one .offerings-full{
      width:100% !important;
      max-width:none !important;
      margin:0 !important;
      padding:0 34px !important;
    }
    .home-one .offerings-head{
      width:min(1440px,100%);
      margin:0 auto 34px !important;
      display:grid !important;
      grid-template-columns:minmax(0,1.15fr) minmax(320px,.85fr) !important;
      gap:72px !important;
      align-items:end !important;
    }
    .home-one .offerings-title-wrap h2{
      max-width:820px;
      margin-top:14px;
      color:#0f1726 !important;
    }
    .home-one .offerings-intro-copy{
      max-width:520px;
      justify-self:end;
    }
    .home-one .offerings-intro-copy p{
      color:#68778a !important;
    }

    .home-one .solutions-toolbar{
      width:min(1440px,100%);
      margin:0 auto 30px !important;
      display:flex !important;
      flex-wrap:nowrap !important;
      justify-content:flex-start !important;
      gap:8px !important;
      padding:7px !important;
      overflow-x:auto !important;
      border:1px solid #dfe7ef !important;
      border-radius:14px !important;
      background:#fff !important;
      box-shadow:0 10px 28px rgba(15,38,63,.05) !important;
      scrollbar-width:none;
    }
    .home-one .solutions-toolbar::-webkit-scrollbar{display:none;}
    .home-one .solution-filter{
      flex:0 0 auto;
      min-height:40px !important;
      padding:0 15px !important;
      border-radius:9px !important;
      border:0 !important;
      background:transparent !important;
      color:#5e6d7e !important;
      font-size:12px !important;
      font-weight:600 !important;
      box-shadow:none !important;
    }
    .home-one .solution-filter.is-active{
      background:var(--uss-blue) !important;
      color:#fff !important;
    }

    .home-one .solutions-grid{
      width:100% !important;
      max-width:none !important;
      display:grid !important;
      grid-template-columns:repeat(4,minmax(0,1fr)) !important;
      gap:16px !important;
      align-items:stretch !important;
    }
    .home-one .solution-card{
      min-width:0 !important;
      border-radius:20px !important;
      overflow:visible !important;
      background:transparent !important;
      box-shadow:none !important;
    }
    .home-one .solution-link{
      position:relative !important;
      min-height:380px !important;
      display:flex !important;
      align-items:flex-end !important;
      overflow:hidden !important;
      border:1px solid #dfe7ef !important;
      border-radius:20px !important;
      background-position:center !important;
      background-size:cover !important;
      box-shadow:none !important;
      transform:none !important;
      transition:transform .22s ease,box-shadow .22s ease,border-color .22s ease !important;
    }
    .home-one .solution-link::before{
      content:"" !important;
      position:absolute !important;
      inset:0 !important;
      background:linear-gradient(180deg,
        rgba(5,20,38,0) 0%,
        rgba(5,20,38,.015) 42%,
        rgba(5,20,38,.18) 62%,
        rgba(5,20,38,.86) 100%) !important;
      z-index:1 !important;
    }
    .home-one .solution-card:hover .solution-link{
      transform:translateY(-5px) !important;
      border-color:#bfd3e5 !important;
      box-shadow:0 24px 50px rgba(11,39,68,.14) !important;
    }

    /* Remove all small category tiles such as People Flow / Access Control. */
    .home-one .solution-chip{
      display:none !important;
    }

    /* New text placement: a clean bottom composition instead of a separate title tile. */
    .home-one .solution-title-bar{
      position:absolute !important;
      z-index:3 !important;
      left:0 !important;
      right:0 !important;
      bottom:0 !important;
      display:block !important;
      padding:70px 22px 22px !important;
      background:linear-gradient(180deg,transparent 0%,rgba(4,18,35,.72) 55%,rgba(4,18,35,.96) 100%) !important;
      border:0 !important;
      transform:none !important;
    }
    .home-one .solution-title-bar h3{
      max-width:90%;
      margin:0 !important;
      color:#fff !important;
      font-size:20px !important;
      line-height:1.18 !important;
      font-weight:700 !important;
      letter-spacing:-.02em !important;
    }

    .home-one .solution-hover{
      position:absolute !important;
      z-index:4 !important;
      inset:auto 12px 12px 12px !important;
      min-height:180px !important;
      display:flex !important;
      flex-direction:column !important;
      justify-content:flex-end !important;
      padding:20px !important;
      border:1px solid rgba(255,255,255,.30) !important;
      border-radius:16px !important;
      background:rgba(5,25,48,.86) !important;
      backdrop-filter:blur(14px) !important;
      box-shadow:0 18px 34px rgba(0,0,0,.18) !important;
      opacity:0 !important;
      transform:translateY(12px) !important;
      transition:opacity .22s ease,transform .22s ease !important;
    }
    .home-one .solution-card:hover .solution-hover{
      opacity:1 !important;
      transform:translateY(0) !important;
    }
    .home-one .solution-card:hover .solution-title-bar{
      opacity:0 !important;
    }
    .home-one .solution-hover h3{
      margin:0 0 9px !important;
      color:#fff !important;
      font-size:19px !important;
      line-height:1.2 !important;
      font-weight:700 !important;
    }
    .home-one .solution-hover p{
      margin:0 0 14px !important;
      color:rgba(255,255,255,.78) !important;
      font-size:12.5px !important;
      line-height:1.6 !important;
    }
    .home-one .solution-more{
      color:#fff !important;
      font-size:12px !important;
      font-weight:700 !important;
    }
    .home-one .solution-more .arrow{color:var(--uss-red) !important;}

    .home-one .solution-mobile-copy{display:none !important;}

    @media (max-width:1280px){
      .home-one .solutions-grid{grid-template-columns:repeat(3,minmax(0,1fr)) !important;}
      .home-one .offerings-full{padding:0 26px !important;}
    }
    @media (max-width:980px){
      .home-one .offerings-head{grid-template-columns:1fr !important;gap:20px !important;}
      .home-one .offerings-intro-copy{justify-self:start;max-width:760px;}
      .home-one .solutions-grid{grid-template-columns:repeat(2,minmax(0,1fr)) !important;}
      .home-one .solution-link{min-height:350px !important;}
    }
    @media (max-width:620px){
      .home-one .offerings-section{padding:78px 0 86px !important;}
      .home-one .offerings-full{padding:0 14px !important;}
      .home-one .solutions-grid{grid-template-columns:1fr !important;gap:14px !important;}
      .home-one .solution-link{min-height:330px !important;}
      .home-one .solution-hover{
        opacity:0 !important;
        pointer-events:none !important;
      }
      .home-one .solution-title-bar{
        opacity:1 !important;
        padding:80px 18px 18px !important;
      }
      .home-one .solution-title-bar h3{font-size:18px !important;}
    }
'''

if MARKER not in text:
    pos = text.rfind('</style>')
    if pos < 0:
        raise SystemExit('No </style> found in home1.html')
    text = text[:pos] + CSS + '\n  ' + text[pos:]
else:
    start = text.index('    /* HOME1 OFFERINGS FULL WIDTH V2 */')
    end = text.find('</style>', start)
    text = text[:start] + CSS + '\n  ' + text[end:]

path.write_text(text, encoding='utf-8')
