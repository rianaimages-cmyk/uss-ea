from pathlib import Path

MARKER='GLOBAL TWO-LINE SECTION TITLES'
CSS=r'''

    /* GLOBAL TWO-LINE SECTION TITLES */
    @media (min-width:981px){
      .why-head{
        display:block !important;
        grid-template-columns:none !important;
        width:100% !important;
        max-width:1080px !important;
      }
      .why-head>div{width:100% !important;max-width:none !important;}

      #who-title,
      #offerings-title,
      #integrated-approach-title,
      #why-uss-title,
      #environments-title,
      #case-studies-title,
      #partners-title,
      #final-cta-title{
        width:100%;
        max-width:1040px;
        text-wrap:balance;
        overflow-wrap:normal;
        word-break:normal;
        hyphens:none;
      }

      #why-uss-title{
        max-width:980px !important;
        font-size:clamp(42px,3.2vw,56px) !important;
        line-height:1.04 !important;
      }

      .section-centered-head{
        max-width:1080px !important;
      }

      .case-head>div:first-child{
        min-width:0;
        width:min(760px,100%);
      }

      .who-copy h2,
      .offerings-title-wrap h2,
      .integrated-copy h2,
      .why-head h2,
      .section-centered-head h2,
      .case-head h2,
      .final-cta-copy h2{
        text-wrap:balance;
      }
    }

    @media (min-width:681px) and (max-width:980px){
      .why-head{
        display:block !important;
        grid-template-columns:none !important;
        width:100% !important;
        max-width:100% !important;
      }
      #who-title,
      #offerings-title,
      #integrated-approach-title,
      #why-uss-title,
      #environments-title,
      #case-studies-title,
      #partners-title,
      #final-cta-title{
        width:100%;
        max-width:100%;
        text-wrap:balance;
        overflow-wrap:normal;
        word-break:normal;
        hyphens:none;
      }
      #why-uss-title{font-size:clamp(38px,5.2vw,50px) !important;line-height:1.05 !important;}
    }
'''

for filename in ('index.html','home1.html'):
    p=Path(filename)
    text=p.read_text(encoding='utf-8')
    if MARKER in text:
        continue
    pos=text.rfind('</style>')
    if pos<0:
        raise SystemExit(f'No </style> in {filename}')
    text=text[:pos]+CSS+'\n  '+text[pos:]
    p.write_text(text,encoding='utf-8')
