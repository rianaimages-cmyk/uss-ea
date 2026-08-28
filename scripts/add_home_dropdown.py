from pathlib import Path
import re

CORRECT_LOGO='https://res.cloudinary.com/dwbjlidhm/image/upload/v1787903501/RIANA_fiunlc.png'
CSS_MARKER='HOME NAV DROPDOWN'
CSS=r'''

    /* HOME NAV DROPDOWN */
    .nav-home-dropdown{
      position:relative;
      display:flex;
      align-items:center;
    }
    .nav-home-trigger{
      display:inline-flex;
      align-items:center;
      gap:7px;
      color:#111;
      font-family:"Arial Narrow","Roboto Condensed",Arial,sans-serif;
      font-size:clamp(14px,.89vw,17px);
      font-weight:800;
      letter-spacing:-.02em;
      line-height:1;
      white-space:nowrap;
    }
    .nav-home-trigger:hover{color:var(--uss-blue);}
    .nav-home-chevron{
      width:7px;
      height:7px;
      border-right:2px solid currentColor;
      border-bottom:2px solid currentColor;
      transform:rotate(45deg) translateY(-2px);
      transition:transform .18s ease;
    }
    .nav-home-dropdown:hover .nav-home-chevron,
    .nav-home-dropdown:focus-within .nav-home-chevron{
      transform:rotate(225deg) translate(-1px,-1px);
    }
    .nav-home-menu{
      position:absolute;
      top:calc(100% + 15px);
      left:50%;
      z-index:60;
      min-width:170px;
      padding:8px;
      border:1px solid #e8edf2;
      border-radius:15px;
      background:#fff;
      box-shadow:0 18px 42px rgba(5,26,49,.16);
      opacity:0;
      visibility:hidden;
      transform:translate(-50%,-7px);
      transition:opacity .18s ease,transform .18s ease,visibility .18s ease;
    }
    .nav-home-dropdown:hover .nav-home-menu,
    .nav-home-dropdown:focus-within .nav-home-menu{
      opacity:1;
      visibility:visible;
      transform:translate(-50%,0);
    }
    .nav-home-menu::before{
      content:"";
      position:absolute;
      left:0;
      right:0;
      top:-17px;
      height:18px;
    }
    .nav-home-menu a{
      display:block;
      padding:12px 13px;
      border-radius:10px;
      color:#111 !important;
      font-size:14px !important;
    }
    .nav-home-menu a:hover,
    .nav-home-menu a.is-active{
      background:#f2f6fa;
      color:var(--uss-blue) !important;
    }
    .mobile-home-group{border-radius:12px;}
    .mobile-home-main{
      display:flex !important;
      align-items:center;
      justify-content:space-between;
    }
    .mobile-home-sub{
      margin:0 8px 5px 20px;
      padding:10px 13px !important;
      border-left:2px solid var(--uss-red);
      border-radius:0 9px 9px 0 !important;
      background:#f7f9fb;
      color:var(--uss-blue) !important;
      font-size:14px !important;
    }
'''

PAIR_RE=re.compile(
    r'<a[^>]*href="(?:index\.html|/|#)"[^>]*>\s*Home\s*</a>\s*'
    r'<a[^>]*href="home1\.html"[^>]*>\s*Home\s*1\s*</a>',
    re.I
)

for filename in ('index.html','home1.html'):
    p=Path(filename)
    text=p.read_text(encoding='utf-8')

    # Correct header logo: use the supplied USS logo instead of the temporary SVG fallback.
    text=text.replace('src="assets/uss-logo.svg"', f'src="{CORRECT_LOGO}"')

    desktop='''<div class="nav-home-dropdown">
<a class="nav-home-trigger" href="index.html">Home <span class="nav-home-chevron" aria-hidden="true"></span></a>
<div class="nav-home-menu"><a href="home1.html"''' + (' class="is-active"' if filename=='home1.html' else '') + '''>Home 1</a></div>
</div>'''

    nav_start=text.find('<nav aria-label="Primary navigation" class="nav-links">')
    nav_end=text.find('</nav>',nav_start)
    if nav_start>=0 and nav_end>nav_start:
        block=text[nav_start:nav_end+6]
        new_block,count=PAIR_RE.subn(desktop,block,count=1)
        if count:
            text=text[:nav_start]+new_block+text[nav_end+6:]

    mobile_start=text.find('<nav aria-label="Mobile navigation" class="mobile-menu">')
    mobile_end=text.find('</nav>',mobile_start)
    if mobile_start>=0 and mobile_end>mobile_start:
        block=text[mobile_start:mobile_end+6]
        mobile='''<div class="mobile-home-group">
<a class="mobile-home-main" href="index.html">Home <span aria-hidden="true">⌄</span></a>
<a class="mobile-home-sub" href="home1.html">Home 1</a>
</div>'''
        new_block,count=PAIR_RE.subn(mobile,block,count=1)
        if count:
            text=text[:mobile_start]+new_block+text[mobile_end+6:]

    if CSS_MARKER not in text:
        pos=text.rfind('</style>')
        if pos<0:
            raise SystemExit(f'No </style> in {filename}')
        text=text[:pos]+CSS+'\n  '+text[pos:]

    p.write_text(text,encoding='utf-8')
