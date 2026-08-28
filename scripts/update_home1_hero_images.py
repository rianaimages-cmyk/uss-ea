from pathlib import Path
import re

FILE = Path('home1.html')
text = FILE.read_text(encoding='utf-8')

IMG1='https://res.cloudinary.com/dwbjlidhm/image/upload/v1787908833/uss_site_1_kukorq.png'
IMG2='https://res.cloudinary.com/dwbjlidhm/image/upload/v1787908834/uss_site_2_kiir1f.png'
IMG3='https://res.cloudinary.com/dwbjlidhm/image/upload/v1787908833/uss_site_3_ehl7cn.png'

# Replace YouTube hero background with three supplied image slides.
hero_pattern = re.compile(r'<div class="hero-video-wrap" aria-hidden="true">.*?</div>\s*<div class="nav-wrap">', re.S)
hero_replacement = f'''<div class="hero-video-wrap hero-image-slider" aria-hidden="true">
  <div class="hero-image-slide is-active" style="background-image:url('{IMG1}')"></div>
  <div class="hero-image-slide" style="background-image:url('{IMG2}')"></div>
  <div class="hero-image-slide" style="background-image:url('{IMG3}')"></div>
</div>
<div class="nav-wrap">'''
text, count = hero_pattern.subn(hero_replacement, text, count=1)
if count != 1:
    raise SystemExit('Could not replace Home 1 hero background block')

# Make the supplied first image the static/reduced-motion fallback.
text = text.replace('background:#06162d url("assets/hero-poster.jpg") center/cover no-repeat;', f'background:#06162d url("{IMG1}") center/cover no-repeat;')
text = text.replace('background:#06162d url("assets/hero-poster.jpg") 70% center/cover no-repeat;', f'background:#06162d url("{IMG1}") 70% center/cover no-repeat;')

MARKER='HOME1 CLOUDINARY HERO SLIDER'
if MARKER not in text:
    css=f'''

    /* {MARKER} */
    .home-one .hero-image-slider{{
      background:#06162d url("{IMG1}") center/cover no-repeat !important;
    }}
    .home-one .hero-image-slide{{
      position:absolute;
      inset:0;
      opacity:0;
      transform:scale(1.025);
      background-position:center center;
      background-size:cover;
      background-repeat:no-repeat;
      transition:opacity 1.25s ease,transform 7s ease;
      will-change:opacity,transform;
    }}
    .home-one .hero-image-slide.is-active{{
      opacity:1;
      transform:scale(1.075);
    }}
    @media (max-width:980px){{
      .home-one .hero-image-slide{{background-position:62% center;}}
    }}
    @media (max-width:680px){{
      .home-one .hero-image-slide{{background-position:68% center;}}
    }}
    @media (prefers-reduced-motion:reduce){{
      .home-one .hero-image-slide{{display:none !important;}}
      .home-one .hero-image-slide:first-child{{display:block !important;opacity:1 !important;transform:none !important;}}
    }}
'''
    pos=text.rfind('</style>')
    if pos < 0:
        raise SystemExit('No </style> found')
    text=text[:pos]+css+'\n  '+text[pos:]

if 'HOME1_HERO_SLIDER_SCRIPT' not in text:
    js='''
<script>
/* HOME1_HERO_SLIDER_SCRIPT */
(function(){
  const slides=[...document.querySelectorAll('.home-one .hero-image-slide')];
  if(slides.length<2 || window.matchMedia('(prefers-reduced-motion: reduce)').matches) return;
  let current=0;
  window.setInterval(function(){
    slides[current].classList.remove('is-active');
    current=(current+1)%slides.length;
    slides[current].classList.add('is-active');
  },4500);
})();
</script>
'''
    text=text.replace('</body>', js+'\n</body>')

FILE.write_text(text, encoding='utf-8')
