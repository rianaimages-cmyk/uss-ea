from pathlib import Path

MARKER = 'FILTERS + ENVIRONMENT CARD SPACING REFINEMENT'
CSS = r'''

    /* FILTERS + ENVIRONMENT CARD SPACING REFINEMENT */
    .solutions-toolbar{
      max-width:1180px !important;
      margin-left:auto !important;
      margin-right:auto !important;
      padding:6px !important;
      gap:6px !important;
      border-radius:14px !important;
    }
    .solution-filter{
      min-height:38px !important;
      padding:0 13px !important;
      font-size:11.5px !important;
      font-weight:500 !important;
      white-space:nowrap !important;
    }

    .environment-grid{
      gap:18px !important;
      align-items:stretch !important;
    }
    .environment-item{
      min-width:0 !important;
      padding:20px 14px !important;
    }
    .environment-item h3{
      font-size:15px !important;
      line-height:1.28 !important;
      font-weight:600 !important;
      letter-spacing:-.01em !important;
      text-align:center !important;
      text-wrap:balance !important;
    }
    .environment-icon{
      margin-bottom:13px !important;
    }

    @media (max-width:980px){
      .environment-grid{gap:14px !important;}
      .environment-item h3{font-size:14px !important;}
    }

    @media (max-width:680px){
      .solutions-toolbar{
        display:grid !important;
        grid-template-columns:repeat(3,minmax(0,1fr)) !important;
        grid-template-rows:repeat(2,auto) !important;
        gap:7px !important;
        width:100% !important;
        max-width:none !important;
        overflow:visible !important;
        padding:7px !important;
      }
      .solution-filter{
        width:100% !important;
        min-width:0 !important;
        min-height:42px !important;
        padding:7px 8px !important;
        white-space:normal !important;
        text-align:center !important;
        font-size:10.5px !important;
        line-height:1.25 !important;
        border-radius:9px !important;
      }

      .environment-grid{
        gap:12px !important;
      }
      .environment-item{
        padding:18px 12px !important;
      }
      .environment-item h3{
        font-size:13px !important;
        line-height:1.24 !important;
      }
      .environment-icon{
        width:44px !important;
        height:44px !important;
        margin-bottom:11px !important;
      }
    }
'''

for filename in ('index.html','home1.html'):
    path = Path(filename)
    text = path.read_text(encoding='utf-8')
    if MARKER not in text:
        pos = text.rfind('</style>')
        if pos < 0:
            raise SystemExit(f'No </style> found in {filename}')
        text = text[:pos] + CSS + '\n  ' + text[pos:]
    path.write_text(text, encoding='utf-8')
