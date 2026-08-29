from pathlib import Path

MARKER='STATS RED DETAILS + LIGHTER OFFERINGS OVERLAY'
CSS=r'''

    /* STATS RED DETAILS + LIGHTER OFFERINGS OVERLAY */
    .stat{
      position:relative;
    }
    .stat::before{
      content:"";
      position:absolute;
      top:0;
      left:30px;
      width:42px;
      height:4px;
      border-radius:0 0 999px 999px;
      background:var(--uss-red);
    }
    .stat strong{
      position:relative;
    }
    .stat strong::after{
      content:"";
      display:inline-block;
      width:7px;
      height:7px;
      margin-left:8px;
      border-radius:50%;
      background:var(--uss-red);
      vertical-align:middle;
      transform:translateY(-2px);
    }

    .solution-link::before{
      background:
        linear-gradient(180deg,
          rgba(5,18,36,.015) 0%,
          rgba(5,18,36,.055) 30%,
          rgba(5,18,36,.18) 58%,
          rgba(5,18,36,.62) 100%) !important;
    }

    @media (max-width:680px){
      .stat::before{left:24px;width:34px;}
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
