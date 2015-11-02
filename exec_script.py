#!/usr/bin/python
import sys
from xmatch.archesxmatch import ArchesXMatch
from configobj import ConfigObj

ax = ArchesXMatch()
settings = ConfigObj('archesxmatch.ini')
req = ax.login(settings['username'], settings['password'])
rm = ax.xmatch(sys.argv[1])
#ax.quit()
