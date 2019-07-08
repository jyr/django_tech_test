import os

from .base import *

DEBUG = True
DJANGO_ENV = 'test'

# Database
# https://docs.djangoproject.com/en/2.0/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.test_sqlite3'),
    }
}
