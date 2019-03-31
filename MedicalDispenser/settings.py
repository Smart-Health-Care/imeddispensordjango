"""
Django settings for MedicalDispenser project.

Generated by 'django-admin startproject' using Django 1.11.11.

For more information on this file, see
https://docs.djangoproject.com/en/1.11/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.11/ref/settings/
"""

import os

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.11/howto/deployment/checklist/
# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = os.environ.get("SECRET_KEY", "4yljy#v)c))5wxdkuw@2bk_lk%hf9*$8g!zkx)r+myp!+e3b9k")
IS_PRODUCTION = os.environ.get("IS_PRODUCTION", False)
# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ['*']
# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'dispenser',
    'doctor',
    'users',
    'widget_tweaks',
    'crispy_forms',
    'dal_select2',
    'dal',
    'rest_framework',
    'cashier',
    'pos',
    'corsheaders'
]

MIDDLEWARE = [
    'corsheaders.middleware.CorsMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]
CORS_ORIGIN_ALLOW_ALL = True

ROOT_URLCONF = 'MedicalDispenser.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, '../../templates')],
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

WSGI_APPLICATION = 'MedicalDispenser.wsgi.application'

# Database
# https://docs.djangoproject.com/en/1.11/ref/settings/#databases

if IS_PRODUCTION:
    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.postgresql_psycopg2',
            'NAME': os.environ['POSTGRES_USER'],
            'USER': os.environ['POSTGRES_USER'],
            'PASSWORD': os.environ['POSTGRES_PASSWORD'],
            'HOST': 'postgres',
            'PORT': os.environ['POSTGRES_PORT']
        }
    }
else:
    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.sqlite3',
            'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
        }
    }

# Password validation
# https://docs.djangoproject.com/en/1.11/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/1.11/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'Asia/Kolkata'

USE_I18N = True

USE_L10N = True

USE_TZ = True

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.11/howto/static-files/

STATIC_URL = '/static/'

STATIC_ROOT = 'staticdir'  # for docker deployment

MEDIA_ROOT = os.path.join(BASE_DIR, 'media')

MEDIA_URL = '/media/'

AUTH_USER_MODEL = 'users.User'

LOGIN_REDIRECT = 'user_dashboard'
LOGIN_URL = 'login'
LOGOUT_URL = 'logout'
LOGOUT_REDIRECT_URL = 'landing_page'

CRISPY_TEMPLATE_PACK = 'bootstrap4'
# MULTICHAIN_USER = 'multichainrpc'
# MULTICHAIN_PASS = '79pgKQusiH3VDVpyzsM6e3kRz6gWNctAwgJvymG3iiuz'
# MULTICHAIN_PORT = '8000'
# MULTICHAIN_ASSET = 'ikash'
# MULTICHAIN_ASSET_NKASH = 'inkash'
# MULTICHAIN_HOST = '192.168.56.3'
# MULTICHAIN_CHAIN = 'dockerchain'
# MULTICHAIN_BURN_ADDRESS = '1XXXXXXXJtXXXXXXVhXXXXXXU6XXXXXXUHj348'

INSTA_MOJO_SALT = '5a38744bcd8847908db2df1a507075d9'
INSTA_MOJO_API_KEY = '17583a21e44a3561341fc2c1a2acc954'
INSTA_MOJO_AUTH_TOKEN = 'e6229891554c3db98e1185fc31ac5f78'

INSTA_MOJO_SALT_TEST = 'f8b93c9043964862847387d044e4e79d'
INSTA_MOJO_API_KEY_TEST = 'test_d0df5b44a987c41dbc7aa75e560'
INSTA_MOJO_AUTH_TOKEN_TEST = 'test_6beb5ae2edb00396e835f8379b4'


# SERVER_URL = 'http://192.168.43.192:8000'
SERVER_URL = 'https://imed.iqube.io'
