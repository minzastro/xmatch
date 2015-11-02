#!/usr/bin/python
import sys
from xmatch.archesxmatch import ArchesXMatch
from configobj import ConfigObj

ax = ArchesXMatch()
settings = ConfigObj('archesxmatch.ini')
req = ax.login(settings['username'], settings['password'])
if sys.argv[1] == ':':
    xlist = ax.list()
    fdata = xlist.content.split('\n')
    for row in fdata:
        if len(row) > 0:
            rm = ax.remove(row.split()[3])
else:
    rm = ax.remove(sys.argv[1])
    print rm
ax.quit()
