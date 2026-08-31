from pathlib import Path

path = Path('home1.html')
text = path.read_text(encoding='utf-8')

MARKER = 'HOME1 INTEGRATED COMMAND CENTER V2'
CSS = r'''

    /* HOME1 INTEGRATED COMMAND CENTER V2 */
    .home-one .integrated-approach{
      position:relative;
      overflow:hidden;
      padding:112px 0 120px !important;
      background:#ffffff !important;
      color:#0f1726 !important;
    }
    .home-one .integrated-approach::before{
      content:"";
      position:absolute;
      width:520px;
      height:520px;
      right:-260px;
      top:-250px;
      border-radius:50%;
      background:radial-gradient(circle,rgba(20,86,141,.08),rgba(20,86,141,0) 68%);
      pointer-events:none;
    }
    .home-one .integrated-grid{
      position:relative;
      z-index:2;
      width:min(1440px,calc(100% - 48px)) !important;
      margin:0 auto !important;
      display:grid !important;
      grid-template-columns:minmax(360px,.82fr) minmax(620px,1.18fr) !important;
      gap:72px !important;
      align-items:center !important;
    }
    .home-one .integrated-copy{
      max-width:620px;
    }
    .home-one .integrated-copy .section-number{
      display:flex;
      align-items:center;
      gap:12px;
      margin-bottom:22px;
      color:var(--uss-red) !important;
      font-size:12px !important;
      font-weight:700 !important;
      letter-spacing:.12em !important;
    }
    .home-one .integrated-copy .section-number::before{
      content:"";
      width:34px;
      height:3px;
      border-radius:999px;
      background:var(--uss-red);
      flex:0 0 auto;
    }
    .home-one .integrated-copy h2{
      max-width:650px !important;
      margin:0 0 26px !important;
      color:#0f1726 !important;
      font-size:var(--section-title-size) !important;
      line-height:1.03 !important;
      font-weight:700 !important;
      letter-spacing:-.04em !important;
      text-wrap:balance !important;
    }
    .home-one .integrated-copy h2 span{color:var(--uss-blue) !important;}
    .home-one .integrated-copy p{
      max-width:590px !important;
      margin:0 0 18px !important;
      color:#67768a !important;
      font-size:15px !important;
      line-height:1.76 !important;
      font-weight:400 !important;
    }

    /* New command-center composition */
    .home-one .integration-visual{
      position:relative !important;
      min-height:auto !important;
      padding:18px !important;
      overflow:hidden !important;
      border:1px solid #dce7f1 !important;
      border-radius:30px !important;
      background:#f5f8fb !important;
      box-shadow:0 28px 70px rgba(10,42,73,.10) !important;
    }
    .home-one .integration-visual::before{
      content:"";
      position:absolute;
      left:-100px;
      top:-110px;
      width:300px;
      height:300px;
      border-radius:50%;
      background:radial-gradient(circle,rgba(20,86,141,.12),rgba(20,86,141,0) 70%);
      pointer-events:none;
    }
    .home-one .integration-hub-card{
      position:relative;
      z-index:2;
      display:grid;
      grid-template-columns:minmax(220px,.7fr) minmax(0,1.3fr);
      gap:18px;
      min-height:180px;
      padding:28px;
      border-radius:22px;
      background:linear-gradient(135deg,#071d37 0%,#0c3f6d 66%,#14568d 100%);
      box-shadow:0 20px 44px rgba(7,29,55,.18);
      color:#fff;
    }
    .home-one .integration-hub-main{
      display:flex;
      flex-direction:column;
      justify-content:center;
      min-width:0;
    }
    .home-one .integration-hub-main strong{
      display:block;
      max-width:260px;
      color:#fff;
      font-size:31px;
      line-height:1.02;
      font-weight:700;
      letter-spacing:-.035em;
    }
    .home-one .integration-hub-main small{
      display:block;
      margin-top:11px;
      color:#6fc8ff;
      font-size:11px;
      line-height:1.35;
      font-weight:700;
      letter-spacing:.16em;
      text-transform:uppercase;
    }
    .home-one .integration-hub-lines{
      position:relative;
      display:grid;
      grid-template-columns:repeat(3,1fr);
      gap:9px;
      align-content:center;
    }
    .home-one .integration-hub-lines span{
      height:8px;
      border-radius:999px;
      background:rgba(255,255,255,.11);
      border:1px solid rgba(255,255,255,.08);
    }
    .home-one .integration-hub-lines span:nth-child(2),
    .home-one .integration-hub-lines span:nth-child(5){background:rgba(226,33,42,.78);}
    .home-one .integration-hub-lines span:nth-child(3),
    .home-one .integration-hub-lines span:nth-child(4){background:rgba(76,185,223,.62);}

    .home-one .integration-system-grid{
      position:relative;
      z-index:2;
      display:grid;
      grid-template-columns:repeat(2,minmax(0,1fr));
      gap:10px;
      margin-top:10px;
    }
    .home-one .integration-system-card{
      position:relative;
      min-height:126px;
      display:flex;
      flex-direction:column;
      justify-content:space-between;
      gap:16px;
      padding:20px 20px 18px 22px;
      overflow:hidden;
      border:1px solid #dfe8f0;
      border-radius:18px;
      background:#fff;
      box-shadow:0 10px 24px rgba(8,35,64,.04);
      transition:transform .2s ease,border-color .2s ease,box-shadow .2s ease;
    }
    .home-one .integration-system-card:hover{
      transform:translateY(-3px);
      border-color:#bad2e5;
      box-shadow:0 16px 32px rgba(8,35,64,.08);
    }
    .home-one .integration-system-card::before{
      content:"";
      position:absolute;
      left:0;
      top:18px;
      bottom:18px;
      width:3px;
      border-radius:0 999px 999px 0;
      background:var(--uss-blue);
    }
    .home-one .integration-system-card:nth-child(3n+2)::before{background:var(--uss-red);}
    .home-one .integration-system-card h3{
      margin:0 !important;
      color:#142035 !important;
      font-size:16px !important;
      line-height:1.22 !important;
      font-weight:600 !important;
      letter-spacing:-.015em !important;
    }
    .home-one .integration-system-card p{
      margin:0 !important;
      color:#6c7b8c !important;
      font-size:12px !important;
      line-height:1.55 !important;
      font-weight:400 !important;
    }
    .home-one .integration-system-card--wide{
      grid-column:1 / -1;
      min-height:112px;
      display:grid;
      grid-template-columns:minmax(180px,.65fr) minmax(0,1.35fr);
      align-items:center;
      gap:28px;
    }

    @media (max-width:1100px){
      .home-one .integrated-grid{
        grid-template-columns:1fr !important;
        gap:42px !important;
      }
      .home-one .integrated-copy{max-width:860px;}
      .home-one .integrated-copy p{max-width:760px !important;}
    }
    @media (max-width:680px){
      .home-one .integrated-approach{padding:76px 0 84px !important;}
      .home-one .integrated-grid{width:calc(100% - 24px) !important;gap:30px !important;}
      .home-one .integrated-copy p{font-size:14px !important;line-height:1.7 !important;}
      .home-one .integration-visual{padding:10px !important;border-radius:22px !important;}
      .home-one .integration-hub-card{
        grid-template-columns:1fr !important;
        min-height:210px;
        padding:22px !important;
        border-radius:18px !important;
      }
      .home-one .integration-hub-main strong{font-size:27px;}
      .home-one .integration-hub-lines{grid-template-columns:repeat(3,1fr);}
      .home-one .integration-system-grid{grid-template-columns:1fr !important;gap:8px !important;}
      .home-one .integration-system-card,
      .home-one .integration-system-card--wide{
        grid-column:auto !important;
        min-height:112px !important;
        display:flex !important;
        padding:18px 18px 16px 20px !important;
      }
      .home-one .integration-system-card h3{font-size:15px !important;}
    }
'''

NEW_SECTION = r'''<section aria-labelledby="integrated-approach-title" class="integrated-approach" id="integrated-security-approach">
<div class="integrated-grid">
<div class="integrated-copy">
<div class="section-number">05 — INTEGRATED SECURITY APPROACH</div>
<h2 id="integrated-approach-title">One partner. <span>Connected systems.</span> Better visibility.</h2>
<p>USS’s strength lies in bringing multiple security and safety technologies together. An integrated connects systems such as surveillance, intrusion detection, fire alarms, access control, parking, public address and other building technologies through a common operating environment.</p>
<p>This helps security and facility teams reduce isolated workflows, improve situational awareness, and respond to events with better context from one central point of control.</p>
</div>
<div aria-label="Connected security systems visual" class="integration-visual">
<div class="integration-hub-card">
<div class="integration-hub-main">
<strong>Integrated Security</strong>
<small>ONE OPERATING ENVIRONMENT</small>
</div>
<div aria-hidden="true" class="integration-hub-lines">
<span></span><span></span><span></span><span></span><span></span><span></span><span></span><span></span><span></span>
</div>
</div>
<div class="integration-system-grid">
<article class="integration-system-card integration-system-card--wide"><h3>Building Technologies</h3><p>HVAC, Lighting, Energy, Elevators &amp; more</p></article>
<article class="integration-system-card"><h3>Surveillance</h3><p>Real-time monitoring and recordings</p></article>
<article class="integration-system-card"><h3>Intrusion Detection</h3><p>Detect threats and unauthorized access</p></article>
<article class="integration-system-card"><h3>Public Address</h3><p>Instant communication in critical moments</p></article>
<article class="integration-system-card"><h3>Fire Alarms</h3><p>Early detection and life safety systems</p></article>
<article class="integration-system-card"><h3>Parking Management</h3><p>Smart parking, guidance and seamless entry</p></article>
<article class="integration-system-card"><h3>Access Control</h3><p>Secure access for people and vehicles</p></article>
</div>
</div>
</div>
</section>'''

# Add / refresh the Home 1-specific CSS override.
if MARKER not in text:
    pos = text.rfind('</style>')
    if pos < 0:
        raise SystemExit('No </style> found in home1.html')
    text = text[:pos] + CSS + '\n  ' + text[pos:]
else:
    start_css = text.index('    /* HOME1 INTEGRATED COMMAND CENTER V2 */')
    end_css = text.find('</style>', start_css)
    text = text[:start_css] + CSS + '\n  ' + text[end_css:]

# Replace only the Home 1 integrated-security section.
section_start = text.find('<section aria-labelledby="integrated-approach-title" class="integrated-approach" id="integrated-security-approach">')
if section_start < 0:
    raise SystemExit('Integrated Security section not found in home1.html')
section_end = text.find('</section>', section_start)
if section_end < 0:
    raise SystemExit('Integrated Security section closing tag not found')
section_end += len('</section>')
text = text[:section_start] + NEW_SECTION + text[section_end:]

path.write_text(text, encoding='utf-8')
