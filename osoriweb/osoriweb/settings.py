"""
Django settings for osoriweb project.

Generated by 'django-admin startproject' using Django 1.11.4.

For more information on this file, see
https://docs.djangoproject.com/en/1.11/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.11/ref/settings/
"""
import pymysql
import os
from secrets import Secret

pymysql.install_as_MySQLdb()

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.11/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
# SECRET_KEY moved into secrets.py
SECRET_KEY = Secret.secret_key
# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ['211.249.63.229','211.249.63.209', '0.0.0.0', 'localhost', 'hyosori.org','211.234.63.232']


# Application definition

INSTALLED_APPS = [
    'website',
    'website.album',
    'website.board',
    'website.project',

    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django_summernote',

]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'osoriweb.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
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

WSGI_APPLICATION = 'osoriweb.wsgi.application'


# Database
# https://docs.djangoproject.com/en/1.11/ref/settings/#databases

DATABASES = {
    'default': {
#        'ENGINE': 'django.db.backends.sqlite3',
#        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),

	'ENGINE': 'django.db.backends.mysql',
	'NAME':'osoridb',
	'USER':'osoriadmin',
	'PASSWORD':'uiophjkl',
	'HOST':'localhost',
	'PORT':''
    }
}


# Password validation
# https://docs.djangoproject.com/en/1.11/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'osoriweb.validators.CustomUserAttributeSimilarityValidator',
    },
    {
        'NAME': 'osoriweb.validators.CustomMinimumLengthValidator',
    },
    {
        'NAME': 'osoriweb.validators.CustomCommonPasswordValidator',
    },
    {
        'NAME': 'osoriweb.validators.CustomNumericPasswordValidator',
    },
]

LOGIN_REDIRECT_URL = '/'
LOGOUT_REDIRECT_URL = '/'

# Internationalization
# https://docs.djangoproject.com/en/1.11/topics/i18n/

LANGUAGE_CODE = 'ko-kr'

TIME_ZONE = 'Asia/Seoul'

USE_I18N = True

USE_L10N = True

USE_TZ = True

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.11/howto/static-files/

STATIC_URL = '/static/'
STATIC_ROOT = os.path.join(BASE_DIR, 'static')

# Media files

MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')

SUMMERNOTE_CONFIG = {
    # Using SummernoteWidget - iframe mode
    'iframe': True,  # or set False to use SummernoteInplaceWidget - no iframe mode

    # Using Summernote Air-mode
    'airMode': False,

    # Use native HTML tags (`<b>`, `<i>`, ...) instead of style attributes
    # (Firefox, Chrome only)
    'styleWithTags': False,

    # Set text direction : 'left to right' is default.
    'direction': 'ltr',

    # Change editor size
    'width': '100%',
    'height': '480',

    # Or, set editor language/locale forcely
    'lang': 'ko-KR',
    # Need authentication while uploading attachments.
    ##'attachment_require_authentication': True,

    # Set `upload_to` function for attachments.
    ##'attachment_upload_to': my_custom_upload_to_func(),

    # Set custom storage class for attachments.
    ##'attachment_storage_class': 'my.custom.storage.class.name',

    # Set custom model for attachments (default: 'django_summernote.Attachment')
    ##'attachment_model': 'my.custom.attachment.model', # must inherit 'django_summernote.AbstractAttachment'

    # Set common css/js media files
    'external_css': (                                             
        '//netdna.bootstrapcdn.com/bootstrap/3.1.1/css/bootstrap.min.css',      
    ),                                                                          
    'external_js': (                                              
        '//code.jquery.com/jquery-1.9.1.min.js',                                
        '//netdna.bootstrapcdn.com/bootstrap/3.1.1/js/bootstrap.min.js',        
    ),

    # You can add custom css/js for SummernoteWidget.
    'css': (
    ),
    'js': (
    ),

    # And also for SummernoteInplaceWidget.
    # !!! Be sure to put {{ form.media }} in template before initiate summernote.
    'css_for_inplace': (
    ),
    'js_for_inplace': (
    ),

    # Codemirror as codeview
    'codemirror': {
            # Please visit http://summernote.org/examples/#codemirror-as-codeview
            'theme': 'monokai',
    },

}
