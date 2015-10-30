#!/usr/bin/python

def get_chi_match(steps, of, complete, join, output=None):
    result = """
xmatch chi2 nStep=%s nMax=%s completeness=%s join=%s
merge pos chi2
""" % (steps, of, complete, join)
    if output != None:
        result = """
%s
save %s votable
""" % (result, output)
    return result
