# el elinditja a masik processt, majd kilep, meghal, de meg igy is futni fog tovabb a masik


#from subprocess import Popen
#Popen(['/usr/bin/python', 'child.py'])

import daemon

from child import do_main_program

with daemon.DaemonContext() as dc:
    do_main_program()