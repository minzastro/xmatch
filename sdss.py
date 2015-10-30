#!/usr/bin/python
from xmatch.catalog import ArchesXmatchCatalog

class SDSSXmatch(ArchesXmatchCatalog):
    """
    """
    def __init__(self):
        ArchesXmatchCatalog.__init__(self)
        self.vizier_catalog = 'V/139/sdss9'
        self.title = 'sdss'
        self.columns = 'SDSS9,_r,objID,RAJ2000,DEJ2000,/(e_)?[ugriz]mag/'

    def _get_galaxy_condition(self):
        return 'mode==1 && cl==3 && Q == 3'
