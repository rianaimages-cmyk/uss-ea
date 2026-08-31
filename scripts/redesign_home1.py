from pathlib import Path

path = Path('home1.html')
text = path.read_text(encoding='utf-8')

START = '/* HOME1 APPROVAL REDESIGN START */'
END = '/* HOME1 APPROVAL REDESIGN END */'

css = r'''

    /* HOME1 APPROVAL REDESIGN START */
    .home-one{
      --h1-navy:#061a31;
      --h1-blue:#14568d;
      --h1-blue-soft:#edf5fb;
      --h1-red:#e2212a;
      --h1-ink:#0f1726;
      --h1-muted:#667386;
      --h1-border:#dfe8f0;
      --h1-surface:#f7f9fc;
      background:#fff;
    }

    /* Keep Home 1 hero content, only refine the approval-layout treatment. */
    .home-one .hero{min-height:780px;}
    .home-one .navbar{
      border:1px solid rgba(255,255,255,.42);
      box-shadow:0 18px 52px rgba(0,0,0,.18);
    }
    .home-one .hero-copy{width:min(720px,62%);}
    .home-one .hero-glass-stats{
      position:absolute;
      left:0;
      right:0;
      bottom:-54px;
      z-index:12;
      width:min(1180px,calc(100% - 48px));
      margin-inline:auto;
      display:grid;
      grid-template-columns:repeat(4,1fr);
      overflow:hidden;
      border:1px solid rgba(255,255,255,.22);
      border-radius:20px;
      background:rgba(5,28,55,.94);
      box-shadow:0 24px 50px rgba(1,14,28,.28);
      backdrop-filter:blur(16px);
    }
    .home-one .hero-glass-stat{
      min-height:110px;
      display:flex;
      align-items:center;
      padding:24px 30px;
      position:relative;
    }
    .home-one .hero-glass-stat:not(:last-child){border-right:1px solid rgba(255,255,255,.16);}
    .home-one .hero-glass-stat::before{
      content:"";
      width:8px;
      height:8px;
      margin-right:14px;
      border-radius:50%;
      background:var(--h1-red);
      box-shadow:0 0 0 6px rgba(226,33,42,.12);
      flex:0 0 auto;
    }
    .home-one .hero-glass-stat strong{
      display:block;
      color:#fff;
      font-size:31px;
      line-height:1;
      margin-bottom:6px;
    }
    .home-one .hero-glass-stat p{color:rgba(255,255,255,.76);font-size:13px;line-height:1.35;font-weight:700;}
    .home-one > .stats-wrap{display:none;}

    /* Trusted brands: same content, approval concept with a single horizontal strip and faded edges. */
    .home-one .trusted-section{
      display:grid;
      grid-template-columns:minmax(230px,300px) minmax(0,1fr);
      align-items:center;
      gap:18px;
      padding:116px max(24px,calc((100vw - 1240px)/2)) 54px;
      background:#fff;
      border-bottom:1px solid #eef2f6;
    }
    .home-one .trusted-section > .shell{
      width:auto;
      margin:0;
    }
    .home-one .trusted-heading{
      display:block;
      margin:0;
    }
    .home-one .trusted-label{
      color:#202938;
      font-size:22px;
      line-height:1.25;
      font-weight:800;
      white-space:normal;
    }
    .home-one .trusted-label::before{display:none;}
    .home-one .trusted-subline{
      margin-top:8px;
      display:flex;
      flex-wrap:wrap;
      gap:8px 14px;
      color:#7a8492;
      font-size:12px;
      font-weight:700;
    }
    .home-one .trusted-subline .text-link{color:var(--h1-blue);}
    .home-one .logo-marquee{
      padding:16px 4px;
      mask-image:linear-gradient(90deg,transparent 0,#000 9%,#000 91%,transparent 100%);
      -webkit-mask-image:linear-gradient(90deg,transparent 0,#000 9%,#000 91%,transparent 100%);
    }
    .home-one .logo-track{gap:46px;animation-duration:32s;align-items:center;}
    .home-one .client-logo-placeholder{
      min-width:auto;
      height:auto;
      padding:0;
      border:0;
      background:transparent;
      box-shadow:none;
      color:#585f69;
      font-size:22px;
      font-weight:900;
      letter-spacing:-.04em;
      opacity:.82;
      white-space:nowrap;
    }
    .home-one .client-logo-placeholder::before,.home-one .client-logo-placeholder::after{display:none;}

    /* Who we are: editorial split card */
    .home-one .who-section{
      padding:104px 0;
      background:var(--h1-surface);
    }
    .home-one .who-grid{
      grid-template-columns:minmax(380px,.95fr) minmax(480px,1.05fr);
      gap:72px;
      align-items:center;
    }
    .home-one .who-collage{
      min-height:550px;
      border-radius:30px;
      overflow:hidden;
      background:#eaf1f7;
      box-shadow:0 24px 70px rgba(12,36,63,.12);
    }
    .home-one .who-image-main{
      inset:0 14% 13% 0;
      border-radius:0 26px 26px 0;
    }
    .home-one .who-image-overlap{
      width:48%;
      height:52%;
      right:0;
      bottom:0;
      border:8px solid var(--h1-surface);
      border-radius:26px 0 0 0;
    }
    .home-one .who-copy{
      padding:18px 0;
    }
    .home-one .section-number{
      color:var(--h1-red);
      font-size:12px;
      font-weight:900;
      letter-spacing:.14em;
    }
    .home-one .who-copy h2,
    .home-one .offerings-head h2,
    .home-one .integrated-copy h2,
    .home-one .section-centered-head h2,
    .home-one .case-head h2{
      color:var(--h1-ink);
      letter-spacing:-.045em;
    }
    .home-one .who-copy h2{font-size:clamp(38px,3.4vw,58px);line-height:1.02;margin:16px 0 26px;}
    .home-one .who-copy p{color:var(--h1-muted);font-size:15px;line-height:1.8;}
    .home-one .who-cta-button{
      background:var(--h1-blue);
      border-radius:12px;
      box-shadow:0 12px 28px rgba(20,86,141,.18);
    }

    /* Offerings: cleaner approval cards, more image-led and less overlay-heavy. */
    .home-one .offerings-section{
      padding:108px 0;
      background:#fff;
    }
    .home-one .offerings-full{width:min(1240px,calc(100% - 48px));margin-inline:auto;}
    .home-one .offerings-head{
      display:grid;
      grid-template-columns:minmax(0,1.1fr) minmax(320px,.9fr);
      gap:72px;
      align-items:end;
      margin-bottom:32px;
    }
    .home-one .offerings-title-wrap h2{font-size:clamp(38px,3.4vw,56px);line-height:1.02;}
    .home-one .offerings-title-wrap .accent{color:var(--h1-blue);}
    .home-one .offerings-intro-copy p{color:var(--h1-muted);line-height:1.75;}
    .home-one .solutions-toolbar{
      justify-content:flex-start;
      gap:8px;
      padding:8px;
      border:1px solid var(--h1-border);
      border-radius:16px;
      background:#f8fafc;
      overflow-x:auto;
      scrollbar-width:none;
      margin-bottom:28px;
    }
    .home-one .solutions-toolbar::-webkit-scrollbar{display:none;}
    .home-one .solution-filter{
      flex:0 0 auto;
      min-height:42px;
      padding:0 15px;
      border:0;
      border-radius:10px;
      background:transparent;
      color:#516072;
      box-shadow:none;
      font-size:12px;
    }
    .home-one .solution-filter.is-active{
      background:var(--h1-blue);
      color:#fff;
    }
    .home-one .solutions-grid{grid-template-columns:repeat(3,minmax(0,1fr));gap:18px;}
    .home-one .solution-card{border-radius:20px;}
    .home-one .solution-link{
      min-height:330px;
      border-radius:20px;
      box-shadow:none;
      border:1px solid #e6edf4;
      background-position:center;
      transition:transform .24s ease,box-shadow .24s ease,border-color .24s ease;
    }
    .home-one .solution-link::before{
      background:linear-gradient(180deg,rgba(4,20,40,.01) 0%,rgba(4,20,40,.03) 42%,rgba(4,20,40,.66) 100%)!important;
    }
    .home-one .solution-card:hover .solution-link{
      transform:translateY(-5px);
      border-color:#cbdced;
      box-shadow:0 20px 44px rgba(12,36,63,.12);
    }
    .home-one .solution-chip{
      top:16px;
      left:16px;
      border:1px solid rgba(255,255,255,.7);
      background:rgba(255,255,255,.9);
      color:var(--h1-blue);
      backdrop-filter:blur(9px);
    }
    .home-one .solution-title-bar{padding:22px;}
    .home-one .solution-title-bar h3{font-size:22px;}
    .home-one .solution-hover{
      background:linear-gradient(180deg,rgba(6,26,49,.08),rgba(6,26,49,.92));
      padding:30px 24px 24px;
    }

    /* Integrated approach: move away from a full dark block to a light technical layout. */
    .home-one .integrated-approach{
      padding:112px 0;
      background:linear-gradient(180deg,#f7fafe 0%,#fff 100%);
      color:var(--h1-ink);
    }
    .home-one .integrated-grid{
      grid-template-columns:minmax(360px,.78fr) minmax(560px,1.22fr);
      gap:72px;
      align-items:center;
    }
    .home-one .integrated-copy h2{
      color:var(--h1-ink);
      font-size:clamp(40px,3.8vw,60px);
      line-height:1;
      margin:18px 0 28px;
    }
    .home-one .integrated-copy h2 span{color:var(--h1-blue);}
    .home-one .integrated-copy p{color:var(--h1-muted);line-height:1.8;}
    .home-one .integration-visual{
      min-height:560px;
      border:1px solid #dce8f1;
      border-radius:32px;
      background:#fff;
      box-shadow:0 24px 70px rgba(20,61,96,.08);
    }

    /* Why USS: premium compact card + accordion. */
    .home-one .why-section{
      padding:104px 0;
      background:#fff;
    }
    .home-one .why-layout-new{
      grid-template-columns:minmax(350px,.76fr) minmax(560px,1.24fr);
      gap:24px;
    }
    .home-one .why-visual-panel{
      min-height:500px;
      border-radius:24px;
      box-shadow:0 20px 52px rgba(6,26,49,.18);
    }
    .home-one .why-accordion{gap:8px;}
    .home-one .why-item-new{
      border-radius:14px;
      border-color:#e0e8ef;
      box-shadow:none;
    }
    .home-one .why-item-new[open]{border-color:#b9d4e9;box-shadow:0 10px 28px rgba(20,61,96,.07);}
    .home-one .why-item-new summary{min-height:74px;}

    /* Process: retain content, turn into an intentional red approval banner. */
    .home-one .process-wrap,
    .home-one .process-section,
    .home-one .process-container{
      border-radius:24px;
    }
    .home-one .process-heading{margin-top:58px;}
    .home-one .process-heading h3{font-size:clamp(28px,2.4vw,40px);letter-spacing:-.03em;}
    .home-one .process-line{
      margin-top:26px;
      padding:30px 28px;
      border-radius:22px;
      background:linear-gradient(105deg,#b9141d 0%,#e2212a 58%,#f03b43 100%);
      box-shadow:0 22px 48px rgba(183,20,29,.2);
    }
    .home-one .process-step h4,
    .home-one .process-step p{color:#fff;}
    .home-one .process-step p{opacity:.82;}
    .home-one .process-number{
      color:#fff!important;
      background:rgba(255,255,255,.08)!important;
      border-color:rgba(255,255,255,.38)!important;
    }
    .home-one .process-connector{background:rgba(255,255,255,.35);}

    /* Environments: compact icon strip. */
    .home-one .environments-section{
      padding:100px 0;
      background:var(--h1-surface);
    }
    .home-one .environments-section .section-centered-head{
      max-width:850px;
      margin:0 auto 34px;
      text-align:left;
    }
    .home-one .environment-grid{
      display:grid;
      grid-template-columns:repeat(5,minmax(0,1fr));
      gap:12px;
      overflow:visible;
    }
    .home-one .environment-item{
      min-width:0;
      min-height:140px;
      padding:22px 16px;
      border:1px solid #e1e9f0;
      border-radius:16px;
      background:#fff;
      box-shadow:none;
      transition:transform .2s ease,border-color .2s ease,box-shadow .2s ease;
    }
    .home-one .environment-item:hover{
      transform:translateY(-4px);
      border-color:#bfd5e7;
      box-shadow:0 14px 28px rgba(20,61,96,.08);
    }
    .home-one .environment-icon{
      width:46px;
      height:46px;
      margin:0 0 16px;
      background:#edf5fb;
      border-radius:12px;
      box-shadow:none;
    }
    .home-one .environment-icon img{width:26px;height:26px;}
    .home-one .environment-item h3{text-align:left;font-size:14px;line-height:1.3;}

    /* Case studies: light card carousel. */
    .home-one .case-studies-section{
      padding:108px 0;
      background:#fff;
    }
    .home-one .case-head{align-items:end;margin-bottom:30px;}
    .home-one .case-head h2{font-size:clamp(38px,3.4vw,56px);line-height:1.03;}
    .home-one .case-carousel-viewport{overflow:hidden;}
    .home-one .case-track{gap:18px;}
    .home-one .case-card{
      border-radius:18px;
      min-height:410px;
      border:1px solid #e1e9f0;
      box-shadow:none;
      overflow:hidden;
    }
    .home-one .case-card::before{
      background:linear-gradient(180deg,transparent 28%,rgba(5,22,43,.88) 100%);
    }
    .home-one .case-card:hover{box-shadow:0 20px 42px rgba(12,36,63,.12);}
    .home-one .case-arrow{
      width:44px;height:44px;border-radius:50%;background:#fff;border:1px solid #dce6ef;color:var(--h1-blue);
      box-shadow:0 8px 22px rgba(10,40,68,.08);
    }

    /* Technology partners: restrained strip rather than a heavy block. */
    .home-one .partners-section{
      padding:88px 0;
      background:#f8fafc;
      border-top:1px solid #edf1f5;
      border-bottom:1px solid #edf1f5;
    }
    .home-one .partners-section .section-centered-head{text-align:left;max-width:1240px;}
    .home-one .partner-marquee{
      margin-top:28px;
      mask-image:linear-gradient(90deg,transparent 0,#000 7%,#000 93%,transparent 100%);
      -webkit-mask-image:linear-gradient(90deg,transparent 0,#000 7%,#000 93%,transparent 100%);
    }

    /* CTA + footer: strong navy finish. */
    .home-one .final-cta{
      background:linear-gradient(110deg,#071c34 0%,#0c3f6d 72%,#14568d 100%)!important;
      border-radius:0;
    }
    .home-one .final-cta::before{
      content:"";
      position:absolute;
      inset:0 auto 0 0;
      width:6px;
      background:var(--h1-red);
    }
    .home-one .uss-contact-banner{
      background:#071a30;
      border-radius:18px;
      overflow:hidden;
      transform:translateY(42px);
      position:relative;
      z-index:4;
    }
    .home-one .site-footer{
      padding-top:100px;
      background:#041424;
    }

    @media (max-width:1100px){
      .home-one .trusted-section{grid-template-columns:1fr;padding-top:105px;}
      .home-one .who-grid,.home-one .integrated-grid{grid-template-columns:1fr;gap:42px;}
      .home-one .solutions-grid{grid-template-columns:repeat(2,minmax(0,1fr));}
      .home-one .environment-grid{grid-template-columns:repeat(3,minmax(0,1fr));}
      .home-one .why-layout-new{grid-template-columns:1fr;}
    }
    @media (max-width:760px){
      .home-one .hero{min-height:760px;}
      .home-one .hero-glass-stats{
        position:relative;
        left:auto;right:auto;bottom:auto;
        width:100%;
        margin-top:34px;
        grid-template-columns:repeat(2,1fr);
      }
      .home-one .hero-glass-stat{min-height:86px;padding:18px;}
      .home-one .hero-glass-stat:nth-child(2){border-right:0;}
      .home-one .hero-glass-stat:nth-child(-n+2){border-bottom:1px solid rgba(255,255,255,.14);}
      .home-one .trusted-section{padding:54px 16px 36px;gap:8px;}
      .home-one .trusted-label{font-size:18px;}
      .home-one .client-logo-placeholder{font-size:18px;}
      .home-one .who-section,.home-one .offerings-section,.home-one .integrated-approach,.home-one .why-section,.home-one .environments-section,.home-one .case-studies-section{padding:72px 0;}
      .home-one .who-grid{gap:28px;}
      .home-one .who-collage{min-height:380px;}
      .home-one .offerings-head{grid-template-columns:1fr;gap:20px;}
      .home-one .solutions-grid{grid-template-columns:1fr;}
      .home-one .solution-link{min-height:300px;}
      .home-one .integration-visual{min-height:420px;}
      .home-one .environment-grid{grid-template-columns:repeat(2,minmax(0,1fr));}
      .home-one .environment-item{min-height:125px;}
      .home-one .process-line{padding:24px 18px;}
      .home-one .uss-contact-banner{transform:none;border-radius:0;}
      .home-one .site-footer{padding-top:58px;}
    }
    @media (max-width:520px){
      .home-one .environment-grid{grid-template-columns:1fr 1fr;}
      .home-one .hero-glass-stats{grid-template-columns:1fr;}
      .home-one .hero-glass-stat:not(:last-child){border-right:0;border-bottom:1px solid rgba(255,255,255,.14);}
      .home-one .hero-glass-stat strong{font-size:26px;}
    }
    /* HOME1 APPROVAL REDESIGN END */
'''

if START in text and END in text:
    a = text.index(START)
    b = text.index(END, a) + len(END)
    text = text[:a] + css.strip() + text[b:]
else:
    pos = text.rfind('</style>')
    if pos < 0:
        raise SystemExit('No </style> tag found in home1.html')
    text = text[:pos] + css + '\n  ' + text[pos:]

path.write_text(text, encoding='utf-8')
