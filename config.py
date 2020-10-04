import os
# basedir = os.path.abspath(os.path.dirname(__file__))
import urllib


# engine = create_engine("mssql+pyodbc:///?odbc_connect=%s" % params)



class Config(object):
    params = urllib.parse.quote_plus('DRIVER={SQL Server Native Client 11.0};SERVER=DESKTOP-I3BMDV4;DATABASE=YenBinhMIS;UID=flask;PWD=123456')
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'doan thu xem'
    SQLALCHEMY_DATABASE_URI = "mssql+pyodbc:///?odbc_connect=%s" % params
    SQLALCHEMY_CHECKMODIFICATIONS = False
