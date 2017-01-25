SQLAlCHEMY_TRACK_MODIFICATIONS = True

DEBUG = True

import os
BASEDIR = os.path.abspath(os.path.dirname(__file__))
APP_SECRET_KEY = '7481bfe8-9b03-41c3-b514-5d14b961683b'
dbpath = os.path.join(BASEDIR, "db")
if not os.path.exists(dbpath):
    os.mkdir(dbpath)
SQLALCHEMY_DTATABASE_URI = "sqlite://%s" % os.path.join(dbpath, "technicity.db")  # NOQA
SQLALCHEMY_DATABASE_name = "technicity"
del os
