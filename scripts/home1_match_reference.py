from pathlib import Path

path = Path('home1.html')
text = path.read_text(encoding='utf-8')

START = '/* HOME1 REFERENCE MATCH START */'
END = '/* HOME1 REFERENCE MATCH END */'

css = r'''

    /* HOME1 REFERENCE MATCH START */
    /* Visual-only refinement. Existing Home 1 copy/content is intentionally unchanged. */
    .home-one{
      --ref-navy:#06192f;
      --ref-navy-2:#0b2b4e;
      --ref-blue:#1467c9;
      --ref-red:#e6242d;
      --ref-ink:#0d1830;
      --ref-muted:#667487;
      --ref-border:#dfe7ef;
      --ref-bg:#ffffff;
      background:#fff;
      color:var(--ref-ink);
    }

    .home-one .shell{width:min(1240px,calc(100% - 48px));}

    /* HERO */
    .home-one .hero{
      min-height:720px;
      background:#06192f;
    }
    .home-one .hero::before{
      background:
        linear-gradient(90deg,rgba(2,14,29,.96) 0%,rgba(3,23,46,.90) 34%,rgba(5,38,72,.48) 62%,rgba(5,38,72,.12) 100%);
    }
    .home-one .nav-wrap{padding-top:18px;}
    .home-one .navbar{
      min-height:68px;
      border-radius:14px;
      padding:8px 12px 8px 18px;
      background:rgba(255,255,255,.98);
      box-shadow:0 12px 34px rgba(0,0,0,.14);
    }
    .home-one .brand img{height:46px;max-width:170px;}
    .home-one .nav-links{gap:20px;}
    .home-one .nav-links a{font-size:13px;}
    .home-one .quote-btn{min-height:44px;padding:0 20px;font-size:13px;}

    .home-one .hero-content{
      min-height:560px;
      padding:74px 0 120px;
    }
    .home-one .hero-copy{width:min(660px,58%);}
    .home-one .hero-copy h1{
      max-width:620px;
      margin-bottom:20px;
      font-size:clamp(48px,4.15vw,66px);
      line-height:1.00;
      letter-spacing:-.05em;
    }
    .home-one .hero-copy h1 .hero-title-line:nth-child(2){color:#1680ff;}
    .home-one .hero-copy p{
      max-width:560px;
      margin-bottom:28px;
      font-size:15px;
      line-height:1.7;
    }
    .home-one .hero-cta{min-height:50px;padding:0 21px;border-radius:8px;font-size:13px;}
    .home-one .hero-cta.primary{background:#1678ed;}
    .home-one .hero-cta.secondary{background:rgba(4,20,39,.35);}

    .home-one .hero-glass-stats{
      position:absolute;
      left:50%;
      right:auto;
      bottom:-52px;
      transform:translateX(-50%);
      width:min(1180px,calc(100% - 48px));
      margin:0;
      grid-template-columns:repeat(4,1fr);
      border:1px solid rgba(255,255,255,.18);
      border-radius:14px;
      background:linear-gradient(90deg,#082541 0%,#0a3156 100%);
      box-shadow:0 20px 44px rgba(0,0,0,.28);
    }
    .home-one .hero-glass-stat{
      min-height:104px;
      padding:22px 28px;
    }
    .home-one .hero-glass-stat::before{
      width:28px;
      height:28px;
      margin-right:15px;
      border:2px solid var(--ref-red);
      border-radius:8px;
      background:transparent;
      box-shadow:none;
    }
    .home-one .hero-glass-stat strong{font-size:30px;}
    .home-one .hero-glass-stat p{font-size:12px;}
    .home-one > .stats-wrap{display:none!important;}

    /* TRUSTED */
    .home-one .trusted-section{
      display:block;
      padding:102px 0 42px;
      border:0;
      background:#fff;
    }
    .home-one .trusted-section > .shell{
      width:min(1240px,calc(100% - 48px));
      margin:0 auto 18px;
    }
    .home-one .trusted-heading{
      display:flex;
      align-items:center;
      justify-content:center;
      gap:20px;
      margin:0;
    }
    .home-one .trusted-label{
      color:#394453;
      font-size:16px;
      font-weight:800;
      text-align:center;
      white-space:nowrap;
    }
    .home-one .trusted-label::before{display:none;}
    .home-one .trusted-subline{display:none;}
    .home-one .logo-marquee{
      width:min(1180px,calc(100% - 48px));
      margin:0 auto;
      padding:10px 0 18px;
      mask-image:linear-gradient(90deg,transparent 0,#000 8%,#000 92%,transparent 100%);
      -webkit-mask-image:linear-gradient(90deg,transparent 0,#000 8%,#000 92%,transparent 100%);
    }
    .home-one .logo-track{gap:56px;animation-duration:34s;align-items:center;}
    .home-one .client-logo-placeholder{
      min-width:auto;
      height:auto;
      padding:0;
      border:0;
      border-radius:0;
      background:transparent;
      box-shadow:none;
      color:#5c626a;
      font-size:20px;
      font-weight:900;
      opacity:.78;
      filter:grayscale(1);
      white-space:nowrap;
    }
    .home-one .client-logo-placeholder::before,.home-one .client-logo-placeholder::after{display:none;}

    /* WHO WE ARE */
    .home-one .who-section{
      padding:84px 0 96px;
      background:#fff;
    }
    .home-one .who-grid{
      grid-template-columns:minmax(430px,.95fr) minmax(460px,1.05fr);
      gap:68px;
      align-items:center;
    }
    .home-one .who-collage{
      min-height:510px;
      border-radius:20px;
      background:#edf3f8;
      box-shadow:none;
    }
    .home-one .who-image-main{border-radius:18px;}
    .home-one .who-image-overlap{border-radius:18px;border-width:6px;}
    .home-one .who-copy h2{
      margin:14px 0 22px;
      font-size:clamp(38px,3.2vw,54px);
      line-height:1.04;
    }
    .home-one .who-copy p{font-size:14px;line-height:1.75;}
    .home-one .who-cta-button{border-radius:8px;}

    /* OFFERINGS */
    .home-one .offerings-section{
      padding:88px 0 96px;
      background:#fff;
    }
    .home-one .offerings-full{width:min(1240px,calc(100% - 48px));}
    .home-one .offerings-head{
      grid-template-columns:minmax(0,.9fr) minmax(300px,.55fr);
      gap:70px;
      align-items:end;
      margin-bottom:26px;
    }
    .home-one .offerings-title-wrap h2{
      max-width:690px;
      font-size:clamp(36px,3.1vw,52px);
      line-height:1.04;
    }
    .home-one .offerings-intro-copy p{font-size:14px;line-height:1.7;}
    .home-one .solutions-toolbar{
      justify-content:flex-start;
      margin-bottom:24px;
      padding:7px;
      border:1px solid #e4eaf0;
      border-radius:12px;
      background:#f8fafc;
      overflow-x:auto;
    }
    .home-one .solution-filter{
      min-height:38px;
      padding:0 14px;
      border:0;
      border-radius:8px;
      font-size:11px;
      box-shadow:none;
    }
    .home-one .solutions-grid{
      grid-template-columns:repeat(4,minmax(0,1fr));
      gap:16px;
    }
    .home-one .solution-link{
      min-height:300px;
      border:1px solid #e4ebf2;
      border-radius:13px;
      box-shadow:none;
    }
    .home-one .solution-link::before{
      background:linear-gradient(180deg,rgba(4,20,40,.01),rgba(4,20,40,.04) 48%,rgba(4,20,40,.58) 100%)!important;
    }
    .home-one .solution-chip{
      top:12px;
      left:12px;
      min-height:30px;
      padding:0 10px;
      border-radius:7px;
      background:rgba(255,255,255,.92);
      color:#176bc4;
      font-size:9px;
    }
    .home-one .solution-title-bar{padding:17px 15px;}
    .home-one .solution-title-bar h3{font-size:17px;line-height:1.12;}
    .home-one .solution-hover{padding:22px 18px 18px;}
    .home-one .solution-hover h3{font-size:17px;}
    .home-one .solution-hover p{font-size:12px;line-height:1.55;}

    /* INTEGRATED APPROACH */
    .home-one .integrated-approach{
      padding:92px 0 104px;
      background:#fff;
      color:var(--ref-ink);
    }
    .home-one .integrated-grid{
      grid-template-columns:minmax(350px,.72fr) minmax(580px,1.28fr);
      gap:66px;
      align-items:center;
    }
    .home-one .integrated-copy h2{
      max-width:470px;
      margin:14px 0 22px;
      font-size:clamp(38px,3.1vw,52px);
      line-height:1.02;
      color:var(--ref-ink);
    }
    .home-one .integrated-copy h2 span{color:var(--ref-blue);}
    .home-one .integrated-copy p{font-size:14px;line-height:1.72;color:var(--ref-muted);}
    .home-one .integration-visual{
      min-height:500px;
      border:0;
      border-radius:0;
      background:transparent;
      box-shadow:none;
    }

    /* WHY USS */
    .home-one .why-section{
      padding:52px 0 92px;
      background:#fff;
    }
    .home-one .why-head{display:none;}
    .home-one .why-layout-new{
      grid-template-columns:minmax(330px,.72fr) minmax(580px,1.28fr);
      gap:22px;
      margin-bottom:32px;
    }
    .home-one .why-visual-panel{
      min-height:430px;
      padding:28px;
      border-radius:14px;
      box-shadow:none;
      background-position:center;
    }
    .home-one .why-visual-title{font-size:31px;max-width:300px;}
    .home-one .why-visual-copy{font-size:12px;}
    .home-one .why-item-new{
      border-radius:8px;
      box-shadow:none;
    }
    .home-one .why-item-new summary{
      grid-template-columns:42px 1fr 34px;
      min-height:66px;
      padding:10px 12px;
    }
    .home-one .why-item-number{width:38px;height:38px;border-radius:7px;font-size:11px;}
    .home-one .why-item-title{font-size:15px;}
    .home-one .why-item-toggle{width:30px;height:30px;font-size:17px;}
    .home-one .why-item-copy{padding:0 48px 16px 66px;font-size:12px;}

    /* PROCESS */
    .home-one .process-heading{
      margin-top:30px!important;
      padding:0 0 12px!important;
      background:transparent!important;
      border-radius:0!important;
    }
    .home-one .process-heading h3{font-size:18px!important;color:var(--ref-red)!important;text-transform:uppercase;letter-spacing:.08em!important;}
    .home-one .process-journey{
      grid-template-columns:repeat(4,minmax(0,1fr))!important;
      gap:0!important;
      padding:24px 20px!important;
      border-radius:12px!important;
      background:linear-gradient(105deg,#b9141d 0%,#e2212a 58%,#ef3e45 100%)!important;
      box-shadow:0 18px 40px rgba(183,20,29,.18)!important;
    }
    .home-one .process-step{
      min-height:170px!important;
      padding:12px 22px!important;
      border:0!important;
      border-radius:0!important;
      background:transparent!important;
      box-shadow:none!important;
      position:relative;
    }
    .home-one .process-step:not(:last-child)::after{
      content:'→';
      position:absolute;
      right:-6px;
      top:42%;
      color:#fff;
      font-size:26px;
      opacity:.8;
    }
    .home-one .process-number{
      width:48px!important;height:48px!important;
      color:#fff!important;background:transparent!important;border-color:rgba(255,255,255,.62)!important;
    }
    .home-one .process-step h4{color:#fff!important;font-size:15px!important;}
    .home-one .process-step p{color:rgba(255,255,255,.82)!important;font-size:11px!important;line-height:1.5!important;}

    /* ENVIRONMENTS */
    .home-one .environments-section{
      padding:76px 0 82px;
      background:#fff;
    }
    .home-one .environments-section .section-centered-head{
      max-width:1240px;
      margin:0 auto 22px;
      text-align:left;
    }
    .home-one .environments-section .section-centered-head h2{font-size:32px;max-width:700px;}
    .home-one .environment-grid{
      display:grid!important;
      grid-template-columns:repeat(9,minmax(0,1fr))!important;
      gap:10px!important;
      overflow:visible!important;
      padding:0!important;
    }
    .home-one .environment-item{
      min-width:0!important;
      min-height:118px;
      padding:16px 12px;
      border:1px solid #e4eaf0;
      border-radius:10px;
      background:#fff;
      box-shadow:none;
    }
    .home-one .environment-icon{
      width:40px!important;height:40px!important;
      margin:0 0 12px!important;
      padding:8px!important;
      border:0!important;
      border-radius:8px!important;
      background:#edf5fb!important;
      box-shadow:none!important;
    }
    .home-one .environment-item h3{font-size:11px;line-height:1.25;text-align:left;}

    /* CASE STUDIES */
    .home-one .case-studies-section{
      padding:78px 0 96px;
      background:#fff;
    }
    .home-one .case-head{margin-bottom:22px;}
    .home-one .case-head h2{font-size:34px;}
    .home-one .case-card{
      min-height:370px;
      border:1px solid #e2e8ef;
      border-radius:12px;
      box-shadow:none;
    }
    .home-one .case-content{padding:18px;}
    .home-one .case-content h3{font-size:17px;}
    .home-one .case-content p{font-size:12px;line-height:1.55;}
    .home-one .case-arrow{width:40px;height:40px;}

    /* PARTNERS */
    .home-one .partners-section{
      padding:58px 0 70px;
      background:#fff;
      border-top:1px solid #edf1f4;
    }
    .home-one .partners-section .section-centered-head{display:none;}
    .home-one .partner-marquee{
      margin-top:0;
      mask-image:linear-gradient(90deg,transparent 0,#000 7%,#000 93%,transparent 100%);
      -webkit-mask-image:linear-gradient(90deg,transparent 0,#000 7%,#000 93%,transparent 100%);
    }

    /* CTA / FOOTER */
    .home-one .final-cta{
      background:linear-gradient(110deg,#071c34 0%,#0c3f6d 72%,#14568d 100%)!important;
    }
    .home-one .footer-contact-shell{
      width:min(1180px,calc(100% - 48px));
    }
    .home-one .site-footer{
      background:#04172a;
      padding-top:92px!important;
    }
    .home-one .footer-contact-banner{
      border-radius:12px!important;
      background:#082947!important;
      box-shadow:0 16px 38px rgba(0,0,0,.22)!important;
    }
    .home-one .footer-contact-brand{background:#0a3156!important;}

    @media (max-width:1100px){
      .home-one .solutions-grid{grid-template-columns:repeat(2,minmax(0,1fr));}
      .home-one .environment-grid{grid-template-columns:repeat(5,minmax(0,1fr))!important;}
      .home-one .who-grid,.home-one .integrated-grid,.home-one .why-layout-new{grid-template-columns:1fr;}
    }
    @media (max-width:760px){
      .home-one .hero{min-height:760px;}
      .home-one .hero-content{padding-bottom:70px;}
      .home-one .hero-copy{width:100%;}
      .home-one .hero-glass-stats{
        position:relative;
        left:auto;bottom:auto;transform:none;
        width:100%;
        margin-top:28px;
        grid-template-columns:repeat(2,1fr);
      }
      .home-one .hero-glass-stat{min-height:82px;padding:16px;}
      .home-one .trusted-section{padding-top:48px;}
      .home-one .trusted-label{font-size:15px;}
      .home-one .offerings-head{grid-template-columns:1fr;gap:18px;}
      .home-one .solutions-grid{grid-template-columns:1fr;}
      .home-one .solution-link{min-height:290px;}
      .home-one .process-journey{grid-template-columns:1fr!important;gap:8px!important;}
      .home-one .process-step:not(:last-child)::after{display:none;}
      .home-one .process-step{min-height:auto!important;border-bottom:1px solid rgba(255,255,255,.16)!important;}
      .home-one .environment-grid{grid-template-columns:repeat(2,minmax(0,1fr))!important;}
      .home-one .site-footer{padding-top:54px!important;}
    }
    /* HOME1 REFERENCE MATCH END */
'''

if START in text and END in text:
    a = text.index(START)
    b = text.index(END, a) + len(END)
    text = text[:a] + css.strip() + text[b:]
else:
    pos = text.rfind('</style>')
    if pos < 0:
        raise SystemExit('No closing style tag found')
    text = text[:pos] + css + '\n  ' + text[pos:]

path.write_text(text, encoding='utf-8')
