apache:
  sites:

    qa.leahmoler.com: 
        template_file: salt://apache/vhosts/standard.tmpl
        template_engine: jinja

    dev.leahmoler.com:
        template_file: salt://apache/vhosts/standard.tmpl
        template_engine: jinja

