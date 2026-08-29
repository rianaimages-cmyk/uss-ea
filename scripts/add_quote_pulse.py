from pathlib import Path

MARKER='SUBTLE QUOTE BUTTON PULSE'
CSS=r'''

    /* SUBTLE QUOTE BUTTON PULSE */
    .quote-btn{
      position:relative;
      isolation:isolate;
    }
    .quote-btn::after{
      content:"";
      position:absolute;
      inset:-5px;
      border:2px solid rgba(226,33,42,.34);
      border-radius:999px;
      opacity:0;
      pointer-events:none;
      z-index:-1;
      animation:quotePulse 2.8s ease-out infinite;
    }
    @keyframes quotePulse{
      0%,68%{
        transform:scale(.98);
        opacity:0;
      }
      76%{
        opacity:.32;
      }
      100%{
        transform:scale(1.10);
        opacity:0;
      }
    }
    @media (prefers-reduced-motion:reduce){
      .quote-btn::after{animation:none;}
    }
'''

for filename in ('index.html','home1.html'):
    path=Path(filename)
    text=path.read_text(encoding='utf-8')
    if MARKER not in text:
        pos=text.rfind('</style>')
        if pos < 0:
            raise SystemExit(f'No </style> found in {filename}')
        text=text[:pos]+CSS+'\n  '+text[pos:]
    path.write_text(text,encoding='utf-8')
