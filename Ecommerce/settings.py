"""
Django settings for Ecommerce project.

Generated by 'django-admin startproject' using Django 3.2.6.

For more information on this file, see
https://docs.djangoproject.com/en/3.2/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/3.2/ref/settings/
"""

import django_heroku
import os
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent
DEBUG = True
# DEBUG = os.environ.get('DEBUG') == True

# ALLOWED_HOSTS = []
ALLOWED_HOSTS = ['https://sysales.herokuapp.com']

SITE_ID = 1

# Application definition

INSTALLED_APPS = [    
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.sites',
    'allauth',
    'allauth.account',
    'allauth.socialaccount',
    'allauth.socialaccount.providers.google',
    'allauth.socialaccount.providers.twitter',
    'rest_framework',
    'colorfield',
    'crispy_forms',    

    'produtos',
    'carrinho',
    'categorias',
    'pedidos',
    'accounts',
    # 'Entra21.produtos',
    # 'Entra21.carrinho',
    # 'Entra21.categorias',
    # 'Entra21.pedidos',
    # 'Entra21.accounts'    
]
MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'whitenoise.middleware.WhiteNoiseMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]
STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'
AUTHENTICATION_BACKENDS = [
    'django.contrib.auth.backends.ModelBackend',
    'allauth.account.auth_backends.AuthenticationBackend',
]
SOCIALACCOUNT_PROVIDERS = {
    'facebook': {
        'METHOD': 'oauth2',
        'SCOPE': ['email', 'public_profile'],
        'AUTH_PARAMS': {'auth_type': 'reauthenticate'},
        'INIT_PARAMS': {'cookie': True},
        'FIELDS': [
            'id',
            'first_name',
            'last_name',
            'middle_name',
            'name',
            'name_format',
            'picture',
            'short_name'
        ],
        'EXCHANGE_TOKEN': True,
        'VERIFIED_EMAIL': False,
        'VERSION': 'v7.0',
    }
}
SOCIALACCOUNT_ADAPTER = 'accounts.adapters.MyCustomAdapter'
ACCOUNT_USER_MODEL_USERNAME_FIELD = 'nome_usuario'
ACCOUNT_EMAIL_REQUIRED = True
ACCOUNT_USERNAME_REQUIRED = False
ACCOUNT_EMAIL_VERIFICATION = "none"
ROOT_URLCONF = 'Ecommerce.urls'
SESSION_ENGINE = 'django.contrib.sessions.backends.signed_cookies'
CACHES = {
    'default': {
        'BACKEND': 'django.core.cache.backends.db.DatabaseCache',
        'LOCATION': 'my_cache_table',
    }
}
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': ['templates'],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'Ecommerce.wsgi.application'

SECRET_KEY = os.environ.get('SECRET_KEY')

REST_FRAMEWORK = {
    'DEFAULT_AUTHENTICATION_CLASSES': [
        'rest_framework.authentication.TokenAuthentication',
    ]
}

AUTH_USER_MODEL = 'accounts.MyUser'

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = False

USE_TZ = True


STATIC_URL = '/static/'
STATICFILES_DIRS = [os.path.join(BASE_DIR, 'static')]

MEDIA_ROOT = os.path.join(BASE_DIR, 'media')
MEDIA_URL = '/media/'

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

LOGIN_REDIRECT_URL = '/'
LOGOUT_REDIRECT_URL = '/login/'

# with open('Ecommerce/local_settings.py') as infile:
#     exec(infile.read())



CRISPY_TEMPLATE_PACK = "bootstrap4"

STATIC_ROOT = os.path.join(BASE_DIR, 'staticfile')

django_heroku.settings(locals())

try:
    from Ecommerce.local_settings import *
except ImportError:
    pass

