from .common import *
import os
DEBUG = True
TEMPLATE_DEBUG = DEBUG

ALLOWED_HOSTS = ['elrincondelmanco.com', 'www.elrincondelmanco.com']


DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'manco',
        'USER': 'manco',
        'PASSWORD': 'yPRyWasQ',
        'HOST':'localhost',
    }
}


STATIC_URL = '/static/'
MEDIA_URL = '/media/'
MEDIA_ROOT = '/home/elrincondelmanco/elrincondelmanco/blog/media/'
STATIC_ROOT = '/home/elrincondelmanco/elrincondelmanco/blog/static/'
PATH = '/home/elrincondelmanco/'

LOGIN_REDIRECT_URL = 'post_list'
