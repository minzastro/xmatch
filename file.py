#!/usr/bin/python
from xmatch.catalog import ArchesXmatchCatalog

class FileXmatch(ArchesXmatchCatalog):
    """
    File catalog
    """
    VIZIER_CATALOG = ''
    TITLE = 'file'
    POSERR = {'type': 'CIRCLE',
                    'param1': "0.01"
             }

    @classmethod
    def run_cone_search(self, filename,columns='',
                        condition=''):
        return """get FileLoader file={0}
{6}
set pos ra={1} dec={2}
{3}
set cols {4}
prefix {5}
""".format(filename,
           self.RAJCOLUMN, self.DEJCOLUMN,
           self.get_poserr(),
           columns, filename.split('.')[0], condition)
