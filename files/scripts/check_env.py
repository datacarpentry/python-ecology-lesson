# Author: Hugo Bowne-Anderson

import sys
from pkgutil import iter_modules


# Thanks @ericmjl for function below.
def check_import(packagename):
    """Checks whether a package is installed"""
    if packagename in (name for _, name, _ in iter_modules()):
        return True
    else:
        return False

all_checks_passed = True

# Throw error if Anaconda is not default Python
assert 'anaconda' in sys.prefix.lower(), ("Anaconda is NOT installed as your "
                                  "default version of Python. Please "
                                  "make sure that is in accordance "
                                  "with the instructions provided.")

# Throw error if Python 3 is not default Python
assert sys.version_info.major >= 3, 'Please install Python 3!'

# Packages necessary for workshop
packages = ['numpy', 'matplotlib', 'pandas', 'jupyter', 'plotnine']

# Throw error if any of the necessary packages is not installed
for p in packages:
    assert check_import(p),\
        ("{0} not present. You may have installed a subset of the"
         "required distribution. Please install the entire Anaconda"
         "distribution").format(p)

if all_checks_passed:
    print("All checks passed. Your Anaconda installation is up and "
          "running and ready for Data Carpentry!")
          