#!/usr/bin/python
from xmatch.catalog import ArchesXmatchCatalog

class TwoMassXmatch(ArchesXmatchCatalog):
    """
    """
    def __init__(self):
        ArchesXmatchCatalog.__init__(self)
        self.vizier_catalog = 'II/246/out'
        self.title = '2mass'
        self.columns = '2MASS,RAJ2000,DEJ2000,/(e_)?[JHK]mag/,/.flg/'
        self.poserr = 'type=ELLIPSE param1=errMaj param2=errMin param3=errPA'

    def _get_galaxy_condition(self):
        return 'Qflg.matches("[ABC][ABCDU]{2}")'
