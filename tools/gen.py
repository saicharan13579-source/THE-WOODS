import json
import os
S=os.path.dirname(os.path.abspath(__file__))+'/'
t=open(S+'app_template.html').read()
t=t.replace('const SITE_LINK=%%SITE_LINK%%, VILLA_LINK=%%VILLA_LINK%%, FILE_ROOT=%%FILE_ROOT%%, DL=%%DLJS%%;','const SITE_LINK=%%SITE_LINK%%, VILLA_LINK=%%VILLA_LINK%%, FILE_ROOT=%%FILE_ROOT%%, DL_ROOT=%%DL_ROOT%%, DL=%%DLJS%%;')
t=t.replace('const cadUrl=c=>FILE_ROOT+c.dir','const cadUrl=c=>DL_ROOT+c.dir')
plots=open(S+'plots.json').read()
def build(portal,site,villa,root,dlroot,dl):
    s=t
    for k,v in {'%%PORTAL%%':json.dumps(portal),'%%SITE_LINK%%':json.dumps(site),'%%VILLA_LINK%%':json.dumps(villa),'%%FILE_ROOT%%':json.dumps(root),'%%DL_ROOT%%':json.dumps(dlroot),'%%DLJS%%':json.dumps(dl),'%%DL%%':dl,'%%PLOTS%%':plots}.items():
        s=s.replace(k,v)
    assert '%%' not in s
    return s
def wrap(s):
    i=s.index('</style>')+len('</style>')
    head='<!doctype html>\n<html lang="en">\n<head>\n<meta charset="utf-8">\n<meta name="viewport" content="width=device-width, initial-scale=1, viewport-fit=cover">\n<meta name="robots" content="noindex, nofollow">\n<meta name="theme-color" content="#2f5d3a">\n'
    return head+s[:i]+'\n</head>\n<body>\n'+s[i:]+'\n</body>\n</html>\n'
R=os.path.dirname(S.rstrip('/'))+'/'
open(R+'index.html','w').write(wrap(build('villa','site.html','index.html','','',' download')))
open(R+'site.html','w').write(wrap(build('site','site.html','index.html','','',' download')).replace('<title>The Woods Drawings</title>','<title>The Woods Site Portal</title>'))
open(S+'artifact.html','w').write(build('villa','#site','#home','','https://saicharan13579-source.github.io/THE-WOODS/',''))
print('generated')
