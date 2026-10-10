#!/usr/bin/env python3
"""Generate the offline single-file calculator from the same shipped page/assets."""
from pathlib import Path
import base64,mimetypes,re
root=Path(__file__).resolve().parents[1]
html=(root/'index.html').read_text()
def css_file(path):
 text=path.read_text()
 text=re.sub(r'@import\s+url\([\'"]\./effects\.css[\'"]\);','',text)
 def inline(match):
  url=match[1].strip('\'"')
  if url.startswith(('data:','http:','https:','#')):return match[0]
  asset=(path.parent/url).resolve()
  mime=mimetypes.guess_type(asset.name)[0] or 'application/octet-stream'
  return 'url("data:'+mime+';base64,'+base64.b64encode(asset.read_bytes()).decode()+'")'
 return re.sub(r'url\(([^)]+)\)',inline,text)
html=re.sub(r'<link rel="icon"[^>]+>','',html)
html=html.replace('<script src="assets/design/theme-init.js"></script>','<script>'+(root/'assets/design/theme-init.js').read_text()+'</script>')
html=html.replace('<script src="assets/design/theme-switch.js"></script>','<script>'+(root/'assets/design/theme-switch.js').read_text()+'</script>')
for name in ['assets/design/tokens.css','assets/design/base.css','assets/css/business.css']:
 css=css_file(root/name)
 if name.endswith('base.css'):css=css_file(root/'assets/design/effects.css')+'\n'+css
 html=html.replace('<link rel="stylesheet" href="'+name+'">','<style>\n'+css+'\n</style>')
html=html.replace('<a class="download-link" href="firmenwagenrechner-standalone.html" download>Standalone-HTML herunterladen</a>','')
html=html.replace('Für die lokale Nutzung: Rechner als einzelne HTML-Datei herunterladen.','Standalone-Version: Gestaltung und Rechner sind in dieser HTML-Datei enthalten.')
html=html.replace('class="brand" href="./"','class="brand" href="#calculator-title"')
(root/'firmenwagenrechner-standalone.html').write_text('\n'.join(line.rstrip() for line in html.splitlines())+'\n')
