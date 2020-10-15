import os
import urllib
from dotenv import load_dotenv
basedir = os.path.abspath(os.path.dirname(__file__))
load_dotenv(os.path.join(basedir, '.env'))
params = urllib.parse.quote_plus(os.environ.get('CONNECTION_STRING'))

class Config(object):
    SECRET_KEY = os.environ.get('SECRET_KEY')
    SQLALCHEMY_DATABASE_URI = "mssql+pyodbc:///?odbc_connect=%s" % params
    SQLALCHEMY_CHECKMODIFICATIONS = False
    DEBUG_TB_INTERCEPT_REDIRECTS = False
    BOOTSTRAP_SERVE_LOCAL = True