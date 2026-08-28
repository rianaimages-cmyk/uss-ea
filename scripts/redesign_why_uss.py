from pathlib import Path

MARKER = 'WHY USS ACCORDION REDESIGN'

CSS = r'''

    /* WHY USS ACCORDION REDESIGN */
    .why-section{
      padding:104px 0 96px;
      background:linear-gradient(180deg,#ffffff 0%,#f7fafc 100%);
      overflow:hidden;
    }
    .why-head{
      max-width:760px;
      margin-bottom:38px;
    }
    .why-head h2{
      margin-top:13px;
      font-size:clamp(38px,3.4vw,58px);
      line-height:1.02;
      letter-spacing:-.045em;
    }
    .why-layout-new{
      display:grid;
      grid-template-columns:minmax(290px,.82fr) minmax(520px,1.18fr);
      gap:28px;
      align-items:stretch;
      margin-bottom:68px;
    }
    .why-visual-panel{
      position:relative;
      min-height:500px;
      overflow:hidden;
      padding:34px;
      border-radius:28px;
      background:
        radial-gradient(circle at 82% 18%,rgba(226,33,42,.22),transparent 26%),
        linear-gradient(145deg,#071c34 0%,#0c3f6d 62%,#14568d 100%);
      color:#fff;
      box-shadow:0 24px 60px rgba(7,35,63,.15);
    }
    .why-visual-panel::before{
      content:"";
      position:absolute;
      width:330px;
      height:330px;
      right:-120px;
      bottom:-120px;
      border-radius:50%;
      border:1px solid rgba(255,255,255,.12);
      box-shadow:0 0 0 52px rgba(255,255,255,.035),0 0 0 104px rgba(255,255,255,.02);
    }
    .why-visual-kicker{
      position:relative;
      z-index:2;
      display:inline-flex;
      align-items:center;
      gap:9px;
      padding:8px 12px;
      border-radius:999px;
      background:rgba(255,255,255,.08);
      color:#9bd5ff;
      font-size:11px;
      font-weight:900;
      text-transform:uppercase;
      letter-spacing:.11em;
    }
    .why-visual-kicker::before{
      content:"";
      width:7px;
      height:7px;
      border-radius:50%;
      background:var(--uss-red);
      box-shadow:0 0 0 4px rgba(226,33,42,.16);
    }
    .why-visual-panel h3{
      position:relative;
      z-index:2;
      max-width:390px;
      margin-top:44px;
      color:#fff;
      font-size:clamp(31px,2.8vw,45px);
      line-height:1.03;
      letter-spacing:-.04em;
    }
    .why-visual-panel p{
      position:absolute;
      z-index:2;
      left:34px;
      right:34px;
      bottom:34px;
      max-width:390px;
      color:rgba(255,255,255,.72);
      font-size:14px;
      line-height:1.65;
    }
    .why-visual-index{
      position:absolute;
      z-index:1;
      right:22px;
      top:32px;
      color:rgba(255,255,255,.075);
      font-size:128px;
      line-height:.8;
      font-weight:900;
      letter-spacing:-.08em;
    }

    .why-accordion{
      display:flex;
      flex-direction:column;
      gap:10px;
    }
    .why-item-new{
      overflow:hidden;
      border:1px solid #dce8f1;
      border-radius:18px;
      background:#fff;
      box-shadow:0 8px 24px rgba(9,36,65,.035);
      transition:border-color .22s ease,box-shadow .22s ease,transform .22s ease;
    }
    .why-item-new[open]{
      border-color:#b9d7eb;
      box-shadow:0 16px 36px rgba(9,36,65,.08);
    }
    .why-item-new:hover{transform:translateY(-1px);}
    .why-item-new summary{
      list-style:none;
      cursor:pointer;
      display:grid;
      grid-template-columns:54px 1fr 40px;
      align-items:center;
      gap:16px;
      min-height:84px;
      padding:14px 16px;
      user-select:none;
    }
    .why-item-new summary::-webkit-details-marker{display:none;}
    .why-item-number{
      width:48px;
      height:48px;
      display:grid;
      place-items:center;
      border-radius:14px;
      background:#eef6fb;
      color:var(--uss-blue);
      font-size:13px;
      font-weight:900;
      letter-spacing:.06em;
    }
    .why-item-new[open] .why-item-number{
      background:var(--uss-blue);
      color:#fff;
    }
    .why-item-title{
      color:#101820;
      font-size:clamp(18px,1.35vw,22px);
      line-height:1.08;
      font-weight:900;
    }
    .why-item-toggle{
      width:36px;
      height:36px;
      display:grid;
      place-items:center;
      justify-self:end;
      border-radius:50%;
      background:#f3f7fa;
      color:var(--uss-blue);
      font-size:22px;
      font-weight:400;
      transition:transform .22s ease,background .22s ease,color .22s ease;
    }
    .why-item-new[open] .why-item-toggle{
      transform:rotate(45deg);
      background:var(--uss-red);
      color:#fff;
    }
    .why-item-copy{
      padding:0 74px 22px 86px;
      color:#627181;
      font-size:14px;
      line-height:1.68;
      animation:whyReveal .22s ease both;
    }
    @keyframes whyReveal{from{opacity:0;transform:translateY(-5px)}to{opacity:1;transform:none}}

    @media (max-width:980px){
      .why-layout-new{grid-template-columns:1fr;}
      .why-visual-panel{min-height:330px;}
      .why-visual-panel p{max-width:560px;}
    }
    @media (max-width:680px){
      .why-section{padding:72px 0;}
      .why-head{margin-bottom:26px;}
      .why-layout-new{gap:16px;margin-bottom:48px;}
      .why-visual-panel{min-height:280px;padding:24px;border-radius:22px;}
      .why-visual-panel h3{margin-top:30px;font-size:30px;}
      .why-visual-panel p{left:24px;right:24px;bottom:24px;font-size:13px;}
      .why-visual-index{font-size:92px;right:18px;top:24px;}
      .why-item-new{border-radius:16px;}
      .why-item-new summary{grid-template-columns:46px 1fr 34px;gap:12px;min-height:76px;padding:12px;}
      .why-item-number{width:42px;height:42px;border-radius:12px;}
      .why-item-title{font-size:17px;}
      .why-item-copy{padding:0 16px 18px 70px;font-size:13px;}
    }
'''

NEW_BLOCK = r'''<div class="why-layout-new">
<div class="why-visual-panel">
<div class="why-visual-kicker">Why USS</div>
<div class="why-visual-index">05</div>
<h3>From security assessment to long-term support</h3>
<p>USS supports clients from initial assessment and solution design through integration, scalability and ongoing system maintenance.</p>
</div>
<div class="why-accordion">
<details class="why-item-new" open>
<summary><span class="why-item-number">01</span><span class="why-item-title">Consultancy &amp; Security Audits</span><span class="why-item-toggle">+</span></summary>
<div class="why-item-copy">USS assesses requirements, risks, and the operating environment before selecting the right technology approach.</div>
</details>
<details class="why-item-new">
<summary><span class="why-item-number">02</span><span class="why-item-title">Bespoke Customized Solutions</span><span class="why-item-toggle">+</span></summary>
<div class="why-item-copy">We configure systems around the needs of the facility rather than forcing every client into the same setup.</div>
</details>
<details class="why-item-new">
<summary><span class="why-item-number">03</span><span class="why-item-title">System Integration</span><span class="why-item-toggle">+</span></summary>
<div class="why-item-copy">Our systems are easily integrated with 3rd party technologies to create a more connected operational environment.</div>
</details>
<details class="why-item-new">
<summary><span class="why-item-number">04</span><span class="why-item-title">Scalable Infrastructure</span><span class="why-item-toggle">+</span></summary>
<div class="why-item-copy">USS deploys scalable systems that adapt as facilities, user requirements and security needs evolve.</div>
</details>
<details class="why-item-new">
<summary><span class="why-item-number">05</span><span class="why-item-title">Support &amp; System Maintenance</span><span class="why-item-toggle">+</span></summary>
<div class="why-item-copy">Our team supports installed systems long after installation to help maintain reliable day-to-day operations.</div>
</details>
</div>
</div>
'''

for filename in ('index.html','home1.html'):
    path = Path(filename)
    text = path.read_text(encoding='utf-8')

    if MARKER not in text:
        pos = text.rfind('</style>')
        if pos < 0:
            raise SystemExit(f'No </style> found in {filename}')
        text = text[:pos] + CSS + '\n  ' + text[pos:]

    section_start = text.find('<section aria-labelledby="why-uss-title" class="why-section" id="why-uss">')
    if section_start < 0:
        raise SystemExit(f'Why USS section not found in {filename}')

    grid_start = text.find('<div class="why-grid">', section_start)
    process_start = text.find('<div class="process-heading">', grid_start)
    if grid_start < 0 or process_start < 0:
        raise SystemExit(f'Why USS grid markers not found in {filename}')

    text = text[:grid_start] + NEW_BLOCK + text[process_start:]
    path.write_text(text, encoding='utf-8')
