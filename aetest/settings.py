"""
Django settings for aetest project.

For more information on this file, see
https://docs.djangoproject.com/en/1.6/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.6/ref/settings/
"""

import django.conf.global_settings as DEFAULT_SETTINGS
from django.contrib.messages import constants as message_constants

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
import os
BASE_DIR = os.path.dirname(os.path.dirname(__file__))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.6/howto/deployment/checklist/

AUTH_USER_MODEL = 'core.UserProfile'
LOGIN_URL = '/login/'

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '!9g-t-m2a+jy4&-gwgo3$+^%y%0$1-#a@xa$cb3!j+w$wp-lyg'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

TEMPLATE_DEBUG = True

INTERNAL_IPS = ('127.0.0.1', '0.0.0.0', '10.0.2.2',)

ALLOWED_HOSTS = ['ae-test.adengage.com']


# Application definition

INSTALLED_APPS = (
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'south',
    'debug_toolbar',
    'widget_tweaks',
    'django_extensions',
    'core',
)

MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
)

ROOT_URLCONF = 'aetest.urls'

WSGI_APPLICATION = 'aetest.wsgi.application'


# Database
# https://docs.djangoproject.com/en/1.6/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'aetest',
        'USER': 'aetest',
    }
}

# Internationalization
# https://docs.djangoproject.com/en/1.6/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.6/howto/static-files/

STATIC_URL = '/static/'

# Maps Django's messaging system CSS classes to match the admin panel notifications classes
MESSAGE_TAGS = {
    message_constants.DEBUG : 'settings',
    message_constants.INFO : 'information',
    message_constants.SUCCESS : 'done',
    message_constants.WARNING : 'warning',
    message_constants.ERROR : 'undone',
}

TEMPLATE_CONTEXT_PROCESSORS = DEFAULT_SETTINGS.TEMPLATE_CONTEXT_PROCESSORS + (
    'django.core.context_processors.request',
)

try:
    from settings_local import *
except ImportError:
    pass
