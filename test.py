#!/usr/bin/python
import sys
from xmatch.catalog import ArchesXmatchCatalog
from xmatch.sdss import SDSSXmatch
from xmatch.twomass import TwoMassXmatch
from xmatch import match

def get_galaxy_data(cls):
    m1 = cls()
    return m1.run_cone_search(10., 10., save=True, condition=m1.get_galaxy_condition())

if __name__ == '__main__':
    print get_galaxy_data(SDSSXmatch)
    print get_galaxy_data(TwoMassXmatch)
    print match.get_chi_match(1, 1, 0.999, 'full')
