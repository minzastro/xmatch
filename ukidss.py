#!/usr/bin/python
from xmatch.catalog import ArchesXmatchCatalog

class UKIDSSXmatch(ArchesXmatchCatalog):
    """
    UKIDSS dr9 LAS
    """
    def __init__(self):
        ArchesXmatchCatalog.__init__(self)
        self.vizier_catalog = 'II/319/las9'
        self.title = 'ukidss'
        self.columns = 'ULAS,RAJ2000,DEJ2000,/(e_)?[YHK]mag/'
        self.poserr = {'type': 'RCD_DEC_ELLIPSE',
                        'param1': "e_RAJ2000==null?0.05:0.001*e_RAJ2000",
                        'param2': "e_DEJ2000==null?0.05:0.001*e_DEJ2000"}

    def _get_galaxy_condition(self):
        return 'm==1 && cl==1'
