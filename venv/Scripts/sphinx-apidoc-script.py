#!c:\users\hh177\desktop\medica~1\bme590~1\venv\scripts\python.exe
# EASY-INSTALL-ENTRY-SCRIPT: 'Sphinx==1.8.1','console_scripts','sphinx-apidoc'
__requires__ = 'Sphinx==1.8.1'
import re
import sys
from pkg_resources import load_entry_point

if __name__ == '__main__':
    sys.argv[0] = re.sub(r'(-script\.pyw?|\.exe)?$', '', sys.argv[0])
    sys.exit(
        load_entry_point('Sphinx==1.8.1', 'console_scripts', 'sphinx-apidoc')()
    )
