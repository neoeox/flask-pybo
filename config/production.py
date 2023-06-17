from config.default import *

SQLALCHEMY_DATABASE_URI = 'sqlite:///{}'.format(os.path.join(BASE_DIR, 'pybo.db'))
SQLALCHEMY_TRACK_MODIFICATIONS = False
SECRET_KEY = b'+[\xb3Km\xf7i\xbc\xb0\xe1\xcc\x94\xcf\x0b\x82#'



