from distutils.core import setup
import sys, os.path

# gather our subversion information and save it; quit if that is all we need
import version
version.__set_svn_version__(fullInfo=False)
if "versiononly" in sys.argv[:2] :
    sys.exit(0)

if not hasattr(sys, 'version_info') or sys.version_info < (2,3,0,'alpha',0):
    raise SystemExit, "Python 2.3 or later required to build pytools."

args = sys.argv[:]

for a in args:
    if a.startswith('--local='):
        dir = os.path.abspath(a.split("=")[1])
        sys.argv.extend([
                "--install-lib="+dir,
                "--install-scripts=%s/pytools" % dir])
        args.remove(a)
        sys.argv.remove(a)


setup(name = "pytools",
      version = "3.0",
      description = "General Use Python Tools",
      author = "Warren Hack, Christopher Hanley",
      author_email = "help@stsci.edu",
      license = "http://www.stsci.edu/resources/software_hardware/pyraf/LICENSE",
      platforms = ["Linux","Solaris","Mac OS X","Win"],
      packages = ['pytools'],  
      package_dir={'pytools':'lib'},
      scripts = ['lib/fitsdiff.py','lib/convertwaiveredfits.py']
      )



