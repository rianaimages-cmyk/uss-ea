from pathlib import Path

MARKER='PROCESS RED BANNER OVERRIDE'
CSS=r'''

    /* PROCESS RED BANNER OVERRIDE */
    .why-section .process-heading{
      margin:52px 0 0 !important;
      padding:42px 54px 14px !important;
      text-align:center !important;
      background:linear-gradient(135deg,#e11f26 0%,#c7141b 55%,#ad1117 100%) !important;
      border-radius:32px 32px 0 0 !important;
      box-shadow:0 26px 60px rgba(171,17,23,.18) !important;
    }
    .why-section .process-heading h3{
      max-width:1000px !important;
      margin:0 auto !important;
      color:#fff !important;
      font-size:clamp(28px,2.35vw,40px) !important;
      line-height:1.1 !important;
    }
    .why-section .process-journey{
      display:grid !important;
      grid-template-columns:repeat(4,minmax(0,1fr)) !important;
      gap:26px !important;
      padding:20px 26px 30px !important;
      border-radius:0 0 32px 32px !important;
      border:1px solid rgba(255,255,255,.12) !important;
      border-top:0 !important;
      background:linear-gradient(135deg,#e11f26 0%,#c7141b 55%,#ad1117 100%) !important;
      box-shadow:0 26px 60px rgba(171,17,23,.18) !important;
      overflow:visible !important;
    }
    .why-section .process-journey::before{display:none !important;}
    .why-section .process-step{
      min-height:260px !important;
      padding:28px 24px 26px !important;
      text-align:left !important;
      border-radius:24px !important;
      background:rgba(255,255,255,.10) !important;
      border:1px solid rgba(255,255,255,.14) !important;
      backdrop-filter:blur(10px);
    }
    .why-section .process-step:not(:last-child)::after{display:none !important;}
    .why-section .process-number{
      margin:0 0 24px !important;
      padding:10px 14px !important;
      background:rgba(255,255,255,.16) !important;
      border:1px solid rgba(255,255,255,.22) !important;
      color:#fff !important;
      box-shadow:none !important;
    }
    .why-section .process-step:last-child .process-number{
      background:#fff !important;
      color:#d51d24 !important;
      border-color:#fff !important;
    }
    .why-section .process-step h4{
      margin-bottom:10px !important;
      color:#fff !important;
      font-size:22px !important;
      line-height:1.08 !important;
    }
    .why-section .process-step p{
      max-width:none !important;
      margin:0 !important;
      color:rgba(255,255,255,.92) !important;
      font-size:14px !important;
      line-height:1.72 !important;
    }

    @media (max-width:980px){
      .why-section .process-heading{padding:34px 28px 12px !important;}
      .why-section .process-journey{grid-template-columns:repeat(2,minmax(0,1fr)) !important;gap:18px !important;padding:18px 18px 20px !important;}
      .why-section .process-step{min-height:220px !important;}
    }
    @media (max-width:680px){
      .why-section .process-heading{margin-top:42px !important;padding:28px 18px 10px !important;border-radius:24px 24px 0 0 !important;}
      .why-section .process-heading h3{font-size:clamp(24px,7vw,32px) !important;}
      .why-section .process-journey{grid-template-columns:1fr !important;gap:14px !important;padding:14px 14px 16px !important;border-radius:0 0 24px 24px !important;}
      .why-section .process-step{min-height:auto !important;padding:22px 18px 20px !important;border-radius:18px !important;}
      .why-section .process-number{margin-bottom:16px !important;}
      .why-section .process-step h4{font-size:20px !important;}
      .why-section .process-step p{font-size:13.5px !important;line-height:1.66 !important;}
    }
'''

for filename in ('index.html','home1.html'):
    p=Path(filename)
    text=p.read_text(encoding='utf-8')
    if MARKER in text:
        continue
    pos=text.rfind('</style>')
    if pos<0:
        raise SystemExit(f'No </style> found in {filename}')
    text=text[:pos]+CSS+'\n  '+text[pos:]
    p.write_text(text,encoding='utf-8')
