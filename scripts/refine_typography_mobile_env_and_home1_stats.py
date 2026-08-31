from pathlib import Path

CSS_MARKER = 'TYPOGRAPHY + MOBILE ENV CAROUSEL + HOME1 GLASS STATS'
JS_MARKER = 'MOBILE ENVIRONMENT AUTOCAROUSEL'

CSS = r'''

    /* TYPOGRAPHY + MOBILE ENV CAROUSEL + HOME1 GLASS STATS */

    /* Lighter, more refined Poppins hierarchy across both homepage concepts */
    body{
      font-family:'Poppins',Arial,Helvetica,sans-serif !important;
      font-weight:400 !important;
    }
    .nav-links a,
    .nav-home-trigger,
    .nav-home-menu a,
    .mobile-menu a,
    .mobile-home-main,
    .mobile-home-sub{
      font-family:'Poppins',Arial,Helvetica,sans-serif !important;
      font-size:14px !important;
      font-weight:500 !important;
      letter-spacing:0 !important;
    }
    .quote-btn,
    .mobile-quote{
      font-weight:600 !important;
    }
    .hero h1,
    .hero-title{
      font-weight:700 !important;
      letter-spacing:-.035em !important;
    }
    .who-copy h2,
    .offerings-title-wrap h2,
    .integrated-copy h2,
    .section-centered-head h2,
    .case-head h2,
    .why-visual-title,
    .final-cta h2{
      font-weight:700 !important;
      letter-spacing:-.035em !important;
    }
    .section-number{
      font-weight:700 !important;
    }
    .solution-title-bar h3,
    .solution-hover h3,
    .environment-item h3,
    .case-card h3,
    .why-item-title,
    .process-step h4{
      font-weight:600 !important;
    }
    .who-copy p,
    .offerings-intro-copy p,
    .integrated-copy p,
    .section-centered-head p,
    .case-card p,
    .why-item-copy,
    .process-step p,
    .final-cta p{
      font-weight:400 !important;
    }

    /* Home 1 hero stats: minimal glassmorphism only — no extra ornamentation */
    .home-one .hero-glass-stats{
      overflow:visible !important;
      gap:12px !important;
      padding:0 !important;
      background:transparent !important;
      border:0 !important;
      box-shadow:none !important;
      backdrop-filter:none !important;
    }
    .home-one .hero-glass-stat{
      min-height:104px !important;
      padding:22px 24px !important;
      display:block !important;
      border:1px solid rgba(255,255,255,.22) !important;
      border-radius:18px !important;
      background:rgba(7,28,51,.34) !important;
      box-shadow:0 16px 36px rgba(0,0,0,.14) !important;
      backdrop-filter:blur(15px) saturate(125%) !important;
      -webkit-backdrop-filter:blur(15px) saturate(125%) !important;
    }
    .home-one .hero-glass-stat:not(:last-child){
      border-right:1px solid rgba(255,255,255,.22) !important;
    }
    .home-one .hero-glass-stat::before,
    .home-one .hero-glass-stat::after{
      display:none !important;
      content:none !important;
    }
    .home-one .hero-glass-stat strong{
      margin:0 0 7px !important;
      color:#fff !important;
      font-size:30px !important;
      line-height:1 !important;
      font-weight:700 !important;
      letter-spacing:-.025em !important;
    }
    .home-one .hero-glass-stat p{
      margin:0 !important;
      color:rgba(255,255,255,.78) !important;
      font-size:12.5px !important;
      line-height:1.45 !important;
      font-weight:400 !important;
    }

    /* Mobile environments: one-card carousel with autoplay and pagination dots */
    .environment-carousel-dots{
      display:none;
    }
    @media (max-width:680px){
      .nav-links a,
      .nav-home-trigger,
      .nav-home-menu a,
      .mobile-menu a,
      .mobile-home-main,
      .mobile-home-sub{
        font-size:15px !important;
        font-weight:500 !important;
      }

      .environments-section .section-centered-head h2{
        font-size:clamp(30px,8vw,38px) !important;
        line-height:1.08 !important;
        font-weight:700 !important;
        letter-spacing:-.035em !important;
      }
      .environments-section .section-centered-head p{
        font-size:14px !important;
        line-height:1.65 !important;
        font-weight:400 !important;
      }

      .environments-section .environment-grid{
        display:flex !important;
        grid-template-columns:none !important;
        gap:14px !important;
        overflow-x:auto !important;
        overflow-y:hidden !important;
        scroll-snap-type:x mandatory !important;
        scroll-behavior:smooth !important;
        scrollbar-width:none !important;
        -ms-overflow-style:none !important;
        padding:6px 9vw 14px !important;
        margin-inline:-9vw !important;
      }
      .environments-section .environment-grid::-webkit-scrollbar{
        display:none !important;
      }
      .environments-section .environment-item{
        flex:0 0 82vw !important;
        min-width:82vw !important;
        max-width:82vw !important;
        min-height:170px !important;
        scroll-snap-align:center !important;
        scroll-snap-stop:always !important;
        padding:26px 22px !important;
        border-radius:18px !important;
      }
      .environments-section .environment-item h3{
        font-size:16px !important;
        line-height:1.35 !important;
        font-weight:600 !important;
      }
      .environments-section .environment-icon{
        width:52px !important;
        height:52px !important;
        margin-bottom:18px !important;
      }
      .environment-carousel-dots{
        display:flex !important;
        align-items:center;
        justify-content:center;
        gap:7px;
        margin-top:14px;
      }
      .environment-carousel-dot{
        appearance:none;
        width:7px;
        height:7px;
        padding:0;
        border:0;
        border-radius:999px;
        background:#cbd6df;
        cursor:pointer;
        transition:width .2s ease,background .2s ease;
      }
      .environment-carousel-dot.is-active{
        width:22px;
        background:var(--uss-red);
      }

      .home-one .hero-glass-stats{
        gap:10px !important;
      }
      .home-one .hero-glass-stat{
        min-height:88px !important;
        padding:18px 20px !important;
        border-radius:15px !important;
      }
      .home-one .hero-glass-stat strong{
        font-size:25px !important;
      }
    }
'''

JS = r'''
<script>
/* MOBILE ENVIRONMENT AUTOCAROUSEL */
(function(){
  const mq = window.matchMedia('(max-width: 680px)');
  const carousels = [];

  function buildCarousel(grid){
    if (grid.dataset.mobileCarouselReady === '1') return;
    const items = Array.from(grid.querySelectorAll('.environment-item'));
    if (!items.length) return;

    grid.dataset.mobileCarouselReady = '1';
    const dots = document.createElement('div');
    dots.className = 'environment-carousel-dots';
    dots.setAttribute('aria-label','Environment carousel pagination');

    items.forEach((item,index) => {
      const dot = document.createElement('button');
      dot.type = 'button';
      dot.className = 'environment-carousel-dot' + (index === 0 ? ' is-active' : '');
      dot.setAttribute('aria-label','Go to environment ' + (index + 1));
      dot.addEventListener('click',() => {
        item.scrollIntoView({behavior:'smooth',block:'nearest',inline:'center'});
      });
      dots.appendChild(dot);
    });
    grid.insertAdjacentElement('afterend',dots);

    let active = 0;
    let timer = null;
    let userPause = false;

    const setActive = (index) => {
      active = Math.max(0,Math.min(index,items.length - 1));
      dots.querySelectorAll('.environment-carousel-dot').forEach((dot,i) => {
        dot.classList.toggle('is-active',i === active);
      });
    };

    const nearestIndex = () => {
      const gridCenter = grid.scrollLeft + grid.clientWidth / 2;
      let best = 0;
      let distance = Infinity;
      items.forEach((item,i) => {
        const center = item.offsetLeft + item.offsetWidth / 2;
        const d = Math.abs(center - gridCenter);
        if (d < distance){ distance = d; best = i; }
      });
      return best;
    };

    const goTo = (index) => {
      const target = items[index];
      if (!target) return;
      grid.scrollTo({left:target.offsetLeft - (grid.clientWidth - target.offsetWidth)/2,behavior:'smooth'});
      setActive(index);
    };

    const start = () => {
      clearInterval(timer);
      if (!mq.matches || userPause || window.matchMedia('(prefers-reduced-motion: reduce)').matches) return;
      timer = setInterval(() => goTo((active + 1) % items.length),3200);
    };

    let scrollTimer;
    grid.addEventListener('scroll',() => {
      clearTimeout(scrollTimer);
      scrollTimer = setTimeout(() => setActive(nearestIndex()),90);
    },{passive:true});

    ['touchstart','pointerdown'].forEach(evt => grid.addEventListener(evt,() => {
      userPause = true;
      clearInterval(timer);
    },{passive:true}));
    ['touchend','pointerup','pointercancel'].forEach(evt => grid.addEventListener(evt,() => {
      userPause = false;
      setTimeout(start,1800);
    },{passive:true}));

    carousels.push({start,stop:() => clearInterval(timer)});
    if (mq.matches) setTimeout(() => goTo(0),100);
    start();
  }

  function init(){
    document.querySelectorAll('.environments-section .environment-grid').forEach(buildCarousel);
  }

  function onModeChange(){
    carousels.forEach(c => mq.matches ? c.start() : c.stop());
  }

  if (document.readyState === 'loading') document.addEventListener('DOMContentLoaded',init);
  else init();
  if (mq.addEventListener) mq.addEventListener('change',onModeChange);
  else mq.addListener(onModeChange);
})();
</script>
'''

for filename in ('index.html','home1.html'):
    path = Path(filename)
    text = path.read_text(encoding='utf-8')

    if CSS_MARKER not in text:
        pos = text.rfind('</style>')
        if pos < 0:
            raise SystemExit(f'No </style> found in {filename}')
        text = text[:pos] + CSS + '\n  ' + text[pos:]

    if JS_MARKER not in text:
        pos = text.rfind('</body>')
        if pos < 0:
            raise SystemExit(f'No </body> found in {filename}')
        text = text[:pos] + JS + '\n' + text[pos:]

    path.write_text(text,encoding='utf-8')
