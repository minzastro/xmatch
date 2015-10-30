#!/usr/bin/python
import tempfile as tmp

class ArchesXmatchCatalog():
    """
    General catalog for XMatch.
    """
    def __init__(self):
        self.vizier_catalog = ''
        self.title = 'unknown'
        self.rajcolumn = 'RAJ2000'
        self.dejcolumn = 'DEJ2000'
        self.poserr = 'type=RCD_DEC_ELLIPSE param1=e_RAJ2000 param2=e_DEJ2000'
        self.columns = ''

    def get_poserr(self):
        if self.poserr != None:
            if type(self.poserr) == str:
                return """set poserr %s""" % self.poserr
            elif type(self.poserr) == dict:
                return 'set poserr %s' % ' '.join('%s=%s' % x for x in self.poserr.iteritems())
        else:
            return ''

    def is_null(self, column, null):
        return "{0}==null?{1}:{0}".format(column, null)

    def _get_galaxy_condition(self):
        return ''

    def get_galaxy_condition(self):
        return 'where %s' % self._get_galaxy_condition()

    def get_file_name(self, temp=False):
        if temp:
            name = tmp.mktemp()
        else:
            name = '%s.vot' % self.title
        return name

    def run_cone_search(self, ra, dec, radius='8arcmin',
                        save=False, temp=False,
                        condition=''):
        save_file = ''
        if save:
            save_file = "save %s votable" % self.get_file_name(temp)
        return """
get VizieRLoader tabname={0} mode=cone center="{1} {2}" radius={3} allcolumns
{9}
set pos ra={4} dec={5}
{6}
set cols {7}
prefix {8}
{10}
""".format(self.vizier_catalog, ra, dec, radius,
           self.rajcolumn, self.dejcolumn,
           self.get_poserr(),
           self.columns, self.title, condition, save_file)

def get_galaxy_data(cls, ra, decl):
    m1 = cls()
    return m1.run_cone_search(ra, decl, save=True, condition=m1.get_galaxy_condition())
