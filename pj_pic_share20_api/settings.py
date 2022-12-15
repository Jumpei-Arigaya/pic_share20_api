"""
Django settings for pj_pic_share20_api project.

Generated by 'django-admin startproject' using Django 4.1.4.

For more information on this file, see
https://docs.djangoproject.com/en/4.1/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/4.1/ref/settings/
"""

# 追加
from decouple import config
from dj_database_url import parse as dburl

from pathlib import Path

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/4.1/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = "django-insecure-42l+(0unm^qp_-w#8r_pm-vh!_5o78vydmar-e9yhz1funry@("

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = False

ALLOWED_HOSTS = ['pic-share20-api.herokuapp.com']
# ALLOWED_HOSTS = ['*']

# 追加
default_dburl = 'sqlite:///' + str(BASE_DIR / "db.sqlite3")

# Application definition

INSTALLED_APPS = [
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
    'pic_share20_api', # 追加
    'rest_framework', # 追加
    'corsheaders', # 追加
    'cloudinary',
    'cloudinary_storage',
]

try:
    from .local_settings import *
except ImportError:
    pass

if not DEBUG:
    CLOUDINARY_STORAGE = {
    'CLOUD_NAME': 'hynpeyums',
    'API_KEY': os.environ['CLOUDINARY_API_KEY'],
    'API_SECRET': os.environ['CLOUDINARY_API_SECRET']
}
    


MIDDLEWARE = [
    'corsheaders.middleware.CorsMiddleware', # 追加
    "django.middleware.security.SecurityMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
]

CORS_ORIGIN_WHITELIST = [
    "http://localhost:3000",
    "https://www.pic-share20.com",
    "http://www.pic-share20.com",
    ]

ROOT_URLCONF = "pj_pic_share20_api.urls"

TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [],
        "APP_DIRS": True,
        "OPTIONS": {
            "context_processors": [
                "django.template.context_processors.debug",
                "django.template.context_processors.request",
                "django.contrib.auth.context_processors.auth",
                "django.contrib.messages.context_processors.messages",
            ],
        },
    },
]

WSGI_APPLICATION = "pj_pic_share20_api.wsgi.application"


# Database
# https://docs.djangoproject.com/en/4.1/ref/settings/#databases

# 変更
DATABASES = {
    'default': config('DATABASE_URL', default=default_dburl, cast=dburl),
}


# Password validation
# https://docs.djangoproject.com/en/4.1/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        "NAME": "django.contrib.auth.password_validation.UserAttributeSimilarityValidator",
    },
    {"NAME": "django.contrib.auth.password_validation.MinimumLengthValidator",},
    {"NAME": "django.contrib.auth.password_validation.CommonPasswordValidator",},
    {"NAME": "django.contrib.auth.password_validation.NumericPasswordValidator",},
]

# REST_FRAMEWORK = { 
#     'DEFAULT_RENDERER_CLASSES': (
#         'rest_framework.renderers.JSONRenderer',
#     ),
# }


# Internationalization
# https://docs.djangoproject.com/en/4.1/topics/i18n/

LANGUAGE_CODE = "ja"

TIME_ZONE = "Asia/Tokyo"

USE_I18N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.1/howto/static-files/

STATIC_URL = "static/"

# 追加
STATIC_ROOT = str(BASE_DIR / 'staticfiles')

# Default primary key field type
# https://docs.djangoproject.com/en/4.1/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"

# 追加
import os

MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')

import cloudinary
import cloudinary.uploader
import cloudinary.api

CLOUDINARY_STORAGE = {
'CLOUD_NAME': 'hynpeyums',
'API_KEY': '883334457251387',
'API_SECRET': '8fqssMTIdRfAO_UbVAubOi0CxeA'
}

DEFAULT_FILE_STORAGE = 'cloudinary_storage.storage.MediaCloudinaryStorage'