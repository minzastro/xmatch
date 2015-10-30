#!/usr/bin/python
from xmatch.catalog import ArchesXmatchCatalog

class CFHTXmatch(ArchesXmatchCatalog):
    """
    CFHT wide (T0007)
    """
    def __init__(self):
        ArchesXmatchCatalog.__init__(self)
        self.vizier_catalog = 'II/317/cfhtls_w'
        self.title = 'cfht'
        self.columns = 'CFHTLS,RAJ2000,DEJ2000,/(e_)?[ugriz]mag/,Sfl,Tfl'
        self.poserr = {'type': 'RCD_DEC_ELLIPSE',
                        'param1': "e_RAJ2000==null?0.05:0.001*e_RAJ2000",
                        'param2': "e_DEJ2000==null?0.05:0.001*e_DEJ2000"}

    def _get_galaxy_condition(self):
        return 'gcl < 0.25'
