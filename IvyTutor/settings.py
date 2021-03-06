"""
Django settings for IvyTutor project.

Generated by 'django-admin startproject' using Django 3.1.6.

For more information on this file, see
https://docs.djangoproject.com/en/3.1/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/3.1/ref/settings/
"""
import os
from pathlib import Path
import environ
import dj_database_url

env = environ.Env()
environ.Env.read_env()

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/3.1/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = env('SECRET_KEY')

# SECURITY WARNING: don't run with debug turned on in production!
TEMPLATE_DEBUG = True
DEBUG = False

ALLOWED_HOSTS = ['']

#HTTPS setting 
SESSION_COOKIE_SECURE = True
CSRF_COOKIE_SECURE = True
SECURE_SSL_REDIRECT = True
#HSTS setting
SECURE_HSTS_SECONDS = 31536000
SECURE_HSTS_PRELOAD = True
SECURE_HSTS_INCLUDE_SUBDOMAINS = True

# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'main.apps.MainConfig',
    'widget_tweaks',
    'django_summernote',
    'captcha',
    'taggit',
    'countable_field',
    'crispy_forms',
    'storages',
    
]
CRISPY_TEMPLATE_PACK = 'uni_form'
AUTH_USER_MODEL = 'main.User'

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

ROOT_URLCONF = 'IvyTutor.urls'


TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR,"main/templates")],
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


# Data
# Database
# https://docs.djangoproject.com/en/3.1/ref/settings/#databases
# Database table error try : manage.py migrate --run-syncdb
DATABASES = {
    # 'default': {
    #     'ENGINE': 'django.db.backends.sqlite3',
    #     'NAME': BASE_DIR / 'db.sqlite3',
    }
# }
DATABASES['default'] = dj_database_url.config(conn_max_age=600)


# Password validation
# https://docs.djangoproject.com/en/3.1/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/3.1/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'America/New_York'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.1/howto/static-files/

MEDIA_ROOT = os.path.join(BASE_DIR,'media')
MEDIA_URL = '/media/'
MEDIA_DIR = os.path.join(BASE_DIR,'media')

STATIC_ROOT = os.path.join(BASE_DIR,'staticfiles')
STATIC_URL = '/static/'
STATICFILES_DIRS = (
  os.path.join(BASE_DIR, 'static/'),
)


#For summer-note only
SUMMERNOTE_THEME = 'bs4'  
X_FRAME_OPTIONS = 'ALLOWALL'
XS_SHARING_ALLOWED_METHODS = ['POST','GET','OPTIONS', 'PUT', 'DELETE']

SUMMERNOTE_CONFIG = {
    # Using SummernoteWidget - iframe mode, default
    'iframe': False,

    'summernote': {

        'width': '500px',
        'height': '200px',

        'lang':"en-US",

        'toolbar': [
            ['font', ['bold', 'underline', 'clear']],
            ['fontname', ['fontname']],
            ['color', ['color']],
            ['para', ['ul', 'ol', 'paragraph']],
           
        ],
    
     'js': ('/static/js/SummerNote.js')
    }
}

# For sendgrid only
ADMIN_EMAIL = env('ADMIN_EMAIL')
NOREPLY_EMAIL=env('NOREPLY_EMAIL')
EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = 'smtp.sendgrid.net'
EMAIL_HOST_USER = 'apikey' 
EMAIL_HOST_PASSWORD = env('SENDGRID_API')
EMAIL_PORT = 587
EMAIL_USE_TLS = True
DEFAULT_FROM_EMAIL = NOREPLY_EMAIL

#AWS S3 setting
AWS_S3_REGION_NAME = env('AWS_S3_REGION_NAME')
AWS_S3_SIGNATURE_VERSION = env('AWS_S3_SIGNATURE_VERSION')
AWS_S3_ADDRESSING_STYLE = env('AWS_S3_ADDRESSING_STYLE')
AWS_ACCESS_KEY_ID = env('AWS_ACCESS_KEY_ID')
AWS_SECRET_ACCESS_KEY = env('AWS_SECRET_ACCESS_KEY')
AWS_STORAGE_BUCKET_NAME = env('AWS_STORAGE_BUCKET_NAME')
AWS_S3_FILE_OVERWRITE = False
AWS_DEFAULT_ACL = None
DEFAULT_FILE_STORAGE = 'storages.backends.s3boto3.S3Boto3Storage' 

