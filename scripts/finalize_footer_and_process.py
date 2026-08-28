from pathlib import Path
import re

CSS_MARKER='FINAL FOOTER + PROCESS PLACEMENT FIX'
CSS=r'''

    /* FINAL FOOTER + PROCESS PLACEMENT FIX */
    .why-section .process-heading{
      margin:64px 0 0 !important;
      padding:46px 56px 16px !important;
      background:linear-gradient(135deg,#e2212a 0%,#c9151d 58%,#ad1017 100%) !important;
      border-radius:34px 34px 0 0 !important;
      text-align:center !important;
      box-shadow:0 24px 58px rgba(173,16,23,.18) !important;
    }
    .why-section .process-heading h3{
      max-width:1100px !important;
      margin:0 auto !important;
      color:#fff !important;
      font-size:clamp(30px,2.45vw,42px) !important;
      line-height:1.1 !important;
    }
    .why-section .process-journey{
      display:grid !important;
      grid-template-columns:repeat(4,minmax(0,1fr)) !important;
      gap:28px !important;
      padding:22px 30px 34px !important;
      background:linear-gradient(135deg,#e2212a 0%,#c9151d 58%,#ad1017 100%) !important;
      border:0 !important;
      border-radius:0 0 34px 34px !important;
      box-shadow:0 24px 58px rgba(173,16,23,.18) !important;
      overflow:visible !important;
    }
    .why-section .process-journey::before{display:none !important;}
    .why-section .process-step{
      min-height:250px !important;
      padding:30px 26px 28px !important;
      text-align:left !important;
      border-radius:24px !important;
      background:rgba(255,255,255,.10) !important;
      border:1px solid rgba(255,255,255,.16) !important;
      box-shadow:none !important;
    }
    .why-section .process-step:not(:last-child)::after{display:none !important;}
    .why-section .process-number{
      width:auto !important;height:auto !important;
      margin:0 0 26px !important;
      padding:10px 14px !important;
      border-radius:999px !important;
      background:rgba(255,255,255,.16) !important;
      border:1px solid rgba(255,255,255,.24) !important;
      color:#fff !important;
      box-shadow:none !important;
    }
    .why-section .process-step:last-child .process-number{
      background:#fff !important;
      color:#d51d24 !important;
      border-color:#fff !important;
    }
    .why-section .process-step h4{
      color:#fff !important;
      font-size:22px !important;
      margin-bottom:11px !important;
    }
    .why-section .process-step p{
      max-width:none !important;
      margin:0 !important;
      color:rgba(255,255,255,.92) !important;
      font-size:14px !important;
      line-height:1.72 !important;
    }

    .site-footer{
      position:relative !important;
      padding-top:72px !important;
      background:#06172b !important;
    }
    .footer-contact-shell{
      width:min(var(--container),calc(100% - 48px));
      margin:0 auto 56px;
    }
    .site-footer .footer-contact-banner{
      margin:0 !important;
      transform:none !important;
      box-shadow:0 22px 52px rgba(0,0,0,.26) !important;
      background:#0a2a4b !important;
    }
    .site-footer .footer-contact-brand{
      background:linear-gradient(145deg,#e2212a,#b9141c) !important;
    }

    @media (max-width:980px){
      .why-section .process-heading{padding:36px 28px 14px !important;}
      .why-section .process-journey{grid-template-columns:repeat(2,minmax(0,1fr)) !important;gap:18px !important;padding:18px 18px 22px !important;}
      .why-section .process-step{min-height:220px !important;}
      .footer-contact-shell{width:min(100% - 30px,var(--container));}
    }
    @media (max-width:680px){
      .why-section .process-heading{margin-top:46px !important;padding:28px 18px 10px !important;border-radius:24px 24px 0 0 !important;}
      .why-section .process-heading h3{font-size:clamp(24px,7vw,32px) !important;}
      .why-section .process-journey{grid-template-columns:1fr !important;gap:14px !important;padding:14px 14px 16px !important;border-radius:0 0 24px 24px !important;}
      .why-section .process-step{min-height:auto !important;padding:22px 18px 20px !important;border-radius:18px !important;}
      .site-footer{padding-top:48px !important;}
      .footer-contact-shell{width:calc(100% - 24px);margin-bottom:40px;}
    }
'''

for filename in ('index.html','home1.html'):
    p=Path(filename)
    text=p.read_text(encoding='utf-8')

    # Move the contact banner from outside the footer into the footer itself.
    pattern=re.compile(r'\n<div class="shell">\n(<div class="footer-contact-banner" aria-label="USS contact information">.*?</div>\n</div>)\n<footer class="site-footer" id="footer">',re.S)
    m=pattern.search(text)
    if m:
        banner=m.group(1)
        replacement='\n<footer class="site-footer" id="footer">\n<div class="footer-contact-shell">\n'+banner+'\n</div>'
        text=pattern.sub(replacement,text,count=1)

    # Ensure banner logo points to an asset that exists in the repo.
    text=text.replace('src="assets/uss-logo.png"','src="assets/uss-logo.svg"')

    if CSS_MARKER not in text:
        pos=text.rfind('</style>')
        if pos<0:
            raise SystemExit(f'No </style> found in {filename}')
        text=text[:pos]+CSS+'\n  '+text[pos:]

    p.write_text(text,encoding='utf-8')
