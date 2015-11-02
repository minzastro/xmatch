#!/usr/bin/python
import sys
from xmatch.archesxmatch import ArchesXMatch
from configobj import ConfigObj

ax = ArchesXMatch()
settings = ConfigObj('archesxmatch.ini')
req = ax.login(settings['username'], settings['password'])
ax.list()
rm = ax.upload(sys.argv[1], sys.argv[2])
#ax.quit()
