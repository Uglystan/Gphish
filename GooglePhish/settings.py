"""
Django settings for GooglePhish project.

Generated by 'django-admin startproject' using Django 3.2.7.

For more information on this file, see
https://docs.djangoproject.com/en/3.2/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/3.2/ref/settings/
"""

from dotenv import load_dotenv
from pathlib import Path
from os import environ
from django.core.management.utils import get_random_secret_key
import os

load_dotenv()

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/3.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = environ.get('DJANGO_SECRET_KEY', get_random_secret_key())

# SECURITY WARNING: don't run with debug turned on in production!
# Set debug to False in production
DEBUG = True if environ.get('DEBUG','False').lower() == 'true' else False

# ALLOWED_HOSTS = environ.get('ALLOWED_HOSTS', '*').split(',')
# CSRF_TRUSTED_ORIGINS_VARIABLE = [origin.strip() for origin in environ.get('CSRF_TRUSTED_ORIGINS','https://dmdhrumilmistry.github.io').split(',')]
ALLOWED_HOSTS = [
    'b91c-185-64-149-75.ngrok-free.app',
    'localhost',
    '127.0.0.1'
]
CSRF_TRUSTED_ORIGINS = [
    'https://b91c-185-64-149-75.ngrok-free.app',
    'https://your-domain.ngrok-free.app',
    'https://domain.localhost.run',
]

# Application definition

INSTALLED_APPS = [
    'Phisher.apps.PhisherConfig',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    "whitenoise.middleware.WhiteNoiseMiddleware",
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'GooglePhish.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [BASE_DIR/'templates'],
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

WSGI_APPLICATION = 'GooglePhish.wsgi.application'


# Database
# https://docs.djangoproject.com/en/3.2/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}


# Password validation
# https://docs.djangoproject.com/en/3.2/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/3.2/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.2/howto/static-files/

STATIC_URL = '/static/'

# Default primary key field type
# https://docs.djangoproject.com/en/3.2/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

# Comment STATICFILES_DIRS if debug is false
STATICFILES_DIRS = [
    os.path.join(BASE_DIR, 'static')
]

# Comment STATIC_ROOT when debug is True
# Never use STATICFILES_DIRS and STATIC_ROOT both at the same time
STATIC_ROOT = os.path.join(BASE_DIR, 'serve_static')

## accept CSRF tokens from different domains
# CSRF_TRUSTED_ORIGINS = CSRF_TRUSTED_ORIGINS_VARIABLE