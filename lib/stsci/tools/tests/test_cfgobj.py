"""This was pytools/utils/cfgobj in pandokia."""
from __future__ import absolute_import

import pprint
import sys

from astropy.utils.data import get_pkg_data_filename

from .. import teal, vtor_checks

PY2K = sys.version_info[0] < 3

if PY2K:
    import StringIO
else:
    import io as StringIO


def test_teal_vtor(tmpdir):
    co = teal.load(get_pkg_data_filename('data/rt_sample.cfg'))
    f = tmpdir.join('output.txt')

    # TEST OBJ LOADING
    f.write("THE CONFIG-OBJ:\n")
    pprint.pprint(co.dict(), stream=f, indent=3, width=999)

    # TEST UNDERSTANDING OF .cfgspc
    cs = co.configspec
    f.write("\nTHE CONFIG-SPEC:\n")
    pprint.pprint(cs.dict(), stream=f, indent=3, width=999)

    # TEST sigStrToKwArgsDict
    f.write("\nsigStrToKwArgsDict:\n")

    for item in sorted(cs.keys()):
        sig = cs[item]
        if isinstance(sig, str):
            f.write("SIGN: " + sig + "\n")
            ddd = vtor_checks.sigStrToKwArgsDict(sig)
            sss = StringIO.StringIO()
            # use pprint (and StringIO) so as to print  it sorted
            pprint.pprint(ddd, sss, width=999)
            f.write("DICT: " + sss.getvalue())  # sss has newline
            sss.close()

    # TEST getPosArgs and getKwdArgs
    f.write("\nTHE POS ARGS:\n")
    f.write(str(co.getPosArgs()) + "\n")
    f.write("\nTHE KWD ARGS:\n")
    pprint.pprint(co.getKwdArgs(), stream=f, indent=3, width=999)

    lines = f.readlines()
    stripped = [l.replace('   ', ' ').replace('  ', ' ').replace('{ ', '{').replace(' }', '}').strip() + '\n' for l in lines]

    with open(get_pkg_data_filename('data/cfgobj_output.ref')) as fref:
        ans = fref.readlines()

    bad_lines = []
    for x, y in zip(stripped, ans):
        if x != y:
            bad_lines.append('{} : {}'.format(x, y))

    if len(bad_lines) > 0:
        raise AssertionError(bad_lines)
