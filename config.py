import os
import urllib
from dotenv import load_dotenv
basedir = os.path.abspath(os.path.dirname(__file__))
load_dotenv(os.path.join(basedir, '.env'))


class Config(object):
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'you-will-never-guess'
    
    params = urllib.parse.quote_plus('DRIVER={SQL Server Native Client 11.0};SERVER=DESKTOP-I3BMDV4;DATABASE=YenBinhMIS;UID=flask;PWD=123456')
    SQLALCHEMY_DATABASE_URI = "mssql+pyodbc:///?odbc_connect=%s" % params
    SQLALCHEMY_CHECKMODIFICATIONS = False
