"""
Django settings for event project.

Generated by 'django-admin startproject' using Django 2.2.2.

For more information on this file, see
https://docs.djangoproject.com/en/2.2/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/2.2/ref/settings/
"""

import os

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/2.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '72y6myzmylso#mny4@^0=x&2sv7#pwe!dzw*s3zz)hlrt@@w!3'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []

MEDIA_ROOT =  os.path.join(BASE_DIR, 'media') 
MEDIA_URL = '/media/'

# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'import_export',
    'event_reg',
    'crispy_forms',
  
]
CRISPY_TEMPLATE_PACK = 'bootstrap4'
MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'event.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': ["templates"],
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

WSGI_APPLICATION = 'event.wsgi.application'


# Database
# https://docs.djangoproject.com/en/2.2/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}


# Password validation
# https://docs.djangoproject.com/en/2.2/ref/settings/#auth-password-validators

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


# Internationalization
# https://docs.djangoproject.com/en/2.2/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/2.2/howto/static-files/

STATIC_URL = '/static/'
MEDIA_ROOT =  os.path.join(BASE_DIR, 'media') 
MEDIA_URL = '/media/'

EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'
LOGIN_REDIRECT_URL = '/'
LOGOUT_REDIRECT_URL = '/'


PAYTM_MERCHANT_KEY = "f3Dg7!qCEu46llS!"
PAYTM_MERCHANT_ID = "tQVQVH71689155287442"
HOST_URL = "http://localhost:8000"
PAYTM_CALLBACK_URL = "/response/"
ACCOUNT_DEFAULT_HTTP_PROTOCOL = "https"


if DEBUG:
    PAYTM_MERCHANT_KEY = "f3Dg7!qCEu46llS!"
    PAYTM_MERCHANT_ID = "tQVQVH71689155287442"
    PAYTM_WEBSITE = 'WEBSTAGING'
    HOST_URL = 'http://localhost:8000'
    '''
    In sandbox enviornment you can use following wallet credentials to login and make payment.
    Mobile Number : 7777777777
    Password : Paytm12345
    OTP: 489871
    This test wallet is topped-up to a balance of 7000 Rs. every 5 minutes.
    '''

EMAIL_HOST = 'mail.vyomamopic.com'
EMAIL_PORT = 587
EMAIL_HOST_USER = '_mainaccount@vyomamopic.com'
EMAIL_HOST_PASSWORD = 'XbH]b@4V6(e^'
EMAIL_USE_TLS = True