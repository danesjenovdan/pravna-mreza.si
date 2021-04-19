from .base import *
import os

DEBUG = os.getenv('DJANGO_DEBUG', False)

try:
    from .local import *
except ImportError:
    pass

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': os.getenv('DB_NAME', 'wagtail'),
        'USER': os.getenv('DB_USERNAME', 'wagtail'),
        'PASSWORD': os.getenv('DB_PASSWORD', 'changeme'),
        'HOST': os.getenv('DB_HOST', 'db'),
        'PORT': '5432',
    }
}

# generate with
# python -c 'from django.core.management.utils import get_random_secret_key; print(get_random_secret_key())'
SECRET_KEY = os.getenv('SECRET_KEY', 'grz#16k(0$_15$92*_95jjzxtwx902j0+z4)!msh431*z()xv4')

#ALLOWED_HOSTS = ['pravna-mreza.si', 'www.pravna-mreza.si']
ALLOWED_HOSTS = ['*']

STATIC_ROOT = os.getenv('STATIC_ROOT', '/static/')
STATIC_URL = os.getenv('STATIC_URL', '/static/')
MEDIA_ROOT = os.getenv('MEDIA_ROOT', '/media/')
MEDIA_URL = os.getenv('MEDIA_URL', '/media/')

LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'handlers': {
        'file': {
            'level': 'DEBUG',
            'class': 'logging.FileHandler',
            'filename': '/app/debug.log',
        },
    },
    'loggers': {
        'django': {
            'handlers': ['file'],
            'level': 'DEBUG',
            'propagate': True,
        },
    },
}
