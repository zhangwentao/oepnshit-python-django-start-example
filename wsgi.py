#!/usr/bin/python
import os,sys

virtenv = os.environ['OPENSHIFT_PYTHON_DIR'] + '/virtenv/'
virtualenv = os.path.join(virtenv, 'bin/activate_this.py')
sys.path.append(os.getcwd()+'/sources/')
try:
    execfile(virtualenv, dict(__file__=virtualenv))
except IOError:
    pass
#
# IMPORTANT: Put any additional includes below this line.  If placed above this
# line, it's possible required libraries won't be in your searchable path
#

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "wedate.settings")
from django.core.wsgi import get_wsgi_application                             
application = get_wsgi_application()
