#!/usr/bin/env python 

import os, sys, time, re 

if __name__ == '__main__' :
    root = 'this-week-in'
    readme_txt = '''
    mkdir %s && cd %s && curl https://raw.githubusercontent.com/%s/__init__/master/start.sh | bash
    ''' % ( root,root,root)
    readme_txt = readme_txt.strip().lstrip ()
    with  open( 'README.md', 'w') as fp :
        fp.write( readme_txt)
        fp.writelines([os.linesep])
    print ('README generated...')
