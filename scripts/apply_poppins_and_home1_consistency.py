from pathlib import Path

FONT_LINK = '<link href="https://fonts.googleapis.com/css2?family=Poppins:wght@400;500;600;700;800;900&display=swap" rel="stylesheet"/>'
MARKER = 'GLOBAL POPPINS + SECTION TYPE SCALE'

GLOBAL_CSS = r'''

    /* GLOBAL POPPINS + SECTION TYPE SCALE */
    :root{
      --section-title-size:clamp(38px,3.25vw,54px);
      --section-title-line:1.04;
      --section-body-size:15px;
      --section-body-line:1.75;
      --card-title-size:20px;
    }
    html,body,button,input,textarea,select{
      font-family:'Poppins',Arial,Helvetica,sans-serif !important;
    }
    .nav-links a,
    .nav-home-trigger,
    .mobile-menu a{
      font-family:'Poppins',Arial,Helvetica,sans-serif !important;
    }

    .who-copy h2,
    .offerings-title-wrap h2,
    .integrated-copy h2,
    .section-centered-head h2,
    .case-head h2,
    .why-visual-title,
    .final-cta h2{
      font-size:var(--section-title-size) !important;
      line-height:var(--section-title-line) !important;
      letter-spacing:-.04em !important;
      font-weight:800 !important;
    }
    .who-copy p,
    .offerings-intro-copy p,
    .integrated-copy p,
    .section-centered-head p,
    .case-card p,
    .why-item-copy,
    .final-cta p{
      font-size:var(--section-body-size);
      line-height:var(--section-body-line);
    }
    .solution-title-bar h3,
    .solution-hover h3,
    .environment-item h3,
    .case-card h3,
    .why-item-title{
      font-size:var(--card-title-size);
      line-height:1.25;
      font-weight:700;
    }
    .section-number{
      font-size:12px !important;
      line-height:1.3;
      font-weight:800 !important;
      letter-spacing:.12em !important;
    }

    @media (max-width:980px){
      :root{
        --section-title-size:clamp(34px,5vw,46px);
        --section-body-size:14.5px;
        --card-title-size:19px;
      }
    }
    @media (max-width:680px){
      :root{
        --section-title-size:clamp(30px,8.5vw,40px);
        --section-body-size:14px;
        --card-title-size:17px;
      }
    }
'''

HOME1_MARKER = 'HOME1 WHO WHITE CONSISTENCY OVERRIDE'
HOME1_CSS = r'''

    /* HOME1 WHO WHITE CONSISTENCY OVERRIDE */
    .home-one .who-section{
      background:#fff !important;
      color:#0f1726 !important;
    }
    .home-one .who-section::before{
      background:
        radial-gradient(circle at 86% 18%,rgba(20,86,141,.07),transparent 24%),
        linear-gradient(180deg,#ffffff 0%,#f8fbfd 100%) !important;
    }
    .home-one .who-section::after{
      border-color:rgba(20,86,141,.07) !important;
      box-shadow:0 0 0 70px rgba(20,86,141,.025),0 0 0 140px rgba(20,86,141,.015) !important;
    }
    .home-one .who-copy .section-number{
      color:var(--uss-blue) !important;
      background:#f3f8fc !important;
      border-color:#dce8f1 !important;
      backdrop-filter:none !important;
    }
    .home-one .who-copy h2{
      color:#0f1726 !important;
      font-size:var(--section-title-size) !important;
      line-height:var(--section-title-line) !important;
      font-weight:800 !important;
      letter-spacing:-.04em !important;
    }
    .home-one .who-copy h2::first-line{color:#0f1726 !important;}
    .home-one .who-copy p{
      color:#627181 !important;
      font-size:var(--section-body-size) !important;
      line-height:var(--section-body-line) !important;
    }
    .home-one .who-copy p a{
      color:var(--uss-blue) !important;
      border-bottom-color:rgba(20,86,141,.35) !important;
    }
    .home-one .who-cta-button{
      background:var(--uss-blue) !important;
      color:#fff !important;
      box-shadow:0 14px 32px rgba(20,86,141,.18) !important;
    }
    .home-one .who-cta-button:hover{
      background:var(--uss-blue-dark) !important;
      color:#fff !important;
    }
    .home-one .who-collage::before{
      background:#f3f7fa !important;
      border-color:#dfe8f0 !important;
      backdrop-filter:none !important;
      box-shadow:0 24px 58px rgba(13,46,76,.10) !important;
    }
    .home-one .who-image{
      border-color:#fff !important;
      box-shadow:0 24px 58px rgba(13,46,76,.14) !important;
    }
    .home-one .who-image-overlap{
      border-color:#fff !important;
    }
    .home-one .who-collage::after{
      background:linear-gradient(90deg,var(--uss-red) 0 34%,#fff 34% 64%,var(--uss-blue) 64% 100%) !important;
      box-shadow:0 8px 24px rgba(13,46,76,.12) !important;
    }
'''

for filename in ('index.html','home1.html'):
    path = Path(filename)
    text = path.read_text(encoding='utf-8')

    if FONT_LINK not in text:
        head_pos = text.find('<style>')
        if head_pos < 0:
            raise SystemExit(f'<style> not found in {filename}')
        text = text[:head_pos] + FONT_LINK + '\n' + text[head_pos:]

    if MARKER not in text:
        style_end = text.rfind('</style>')
        if style_end < 0:
            raise SystemExit(f'</style> not found in {filename}')
        text = text[:style_end] + GLOBAL_CSS + '\n  ' + text[style_end:]

    if filename == 'home1.html' and HOME1_MARKER not in text:
        style_end = text.rfind('</style>')
        text = text[:style_end] + HOME1_CSS + '\n  ' + text[style_end:]

    path.write_text(text, encoding='utf-8')
