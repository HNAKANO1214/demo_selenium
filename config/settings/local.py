from .base import *     # noqa: F401, F403
from .base import INSTALLED_APPS, MIDDLEWARE


# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-^%+%#h+w_ol_n38ktl6o-whv39)^a5hc-*f&-w7+k)i6!g=0hw'

ALLOWED_HOSTS = []

INSTALLED_APPS += ['debug_toolbar']
INTERNAL_IPS = ['127.0.0.1']
MIDDLEWARE += ['debug_toolbar.middleware.DebugToolbarMiddleware']
DEBUG_TOOLBAR_CONFIG = {
    "SHOW_TOOLBAR_CALLBACK": lambda request: True,
}
