#coding:utf-8
"""
Django settings for mysite project.

Generated by 'django-admin startproject' using Django 1.8.3.

For more information on this file, see
https://docs.djangoproject.com/en/1.8/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.8/ref/settings/
"""

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
import os,sys

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))



#sys.path.append(os.path.join(os.path.dirname(file), 'lib'))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.8/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'dfx2y6#4(_u*i@fx=_^6w3rw(q7&wot#(zlow%59gd1w-r2=yj'

# SECURITY WARNING: don't run with debug turned on in production!
if 'SERVER_SOFTWARE' in os.environ:
    DEBUG = False
else:
    DEBUG = True

ALLOWED_HOSTS = ["*"]



# Application definition

INSTALLED_APPS = (
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.sitemaps',
    'blog',
)

MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',

    # admin page convert chinese
    'django.middleware.locale.LocaleMiddleware',

    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.auth.middleware.SessionAuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'django.middleware.security.SecurityMiddleware',
)

ROOT_URLCONF = 'mysite.urls'

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

WSGI_APPLICATION = 'mysite.wsgi.application'


# Database
# https://docs.djangoproject.com/en/1.8/ref/settings/#databases


if 'SERVER_SOFTWARE' in os.environ:
    from sae.const import (
        MYSQL_HOST, MYSQL_PORT, MYSQL_USER, MYSQL_PASS, MYSQL_DB
    )
else:
    # Make `python manage.py syncdb` works happy!
    MYSQL_HOST = 'localhost'
    MYSQL_PORT = '3306'
    MYSQL_USER = 'root'
    MYSQL_PASS = 'root'
    MYSQL_DB   = 'ziiblog'


DATABASES = {
    'default': {
        'ENGINE':   'django.db.backends.mysql',
        'NAME':     MYSQL_DB,
        'USER':     MYSQL_USER,
        'PASSWORD': MYSQL_PASS,
        'HOST':     MYSQL_HOST,
        'PORT':     MYSQL_PORT,
    }
}

DATABASES = { 
    'default': {
        # 'ENGINE': 'django.db.backends.sqlite3',
        # 'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
         'ENGINE': 'django.db.backends.mysql',
         'NAME': MYSQL_DB,    ## 数据库名称
         'USER': MYSQL_USER,
         'PASSWORD': MYSQL_PASS, ## 安装 mysql 数据库时，输入的 root 用户的密码
         'HOST': MYSQL_HOST,
    }   
}

# Internationalization
# https://docs.djangoproject.com/en/1.8/topics/i18n/

LANGUAGE_CODE = 'zh-cn'

TIME_ZONE = 'Asia/Shanghai'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.8/howto/static-files/

STATIC_URL = '/static/'
STATICFILES_DIRS = (
    os.path.join(BASE_DIR, "static"),
)

LOGIN_REDIRECT_URL = '/blog/'


# 修改上传时文件在内存中可以存放的最大size为10m
FILE_UPLOAD_MAX_MEMORY_SIZE = 10485760

# sae的本地文件系统是只读的，修改django的file storage backend为Storage
DEFAULT_FILE_STORAGE = 'sae.ext.django.storage.backend.Storage'
# 使用media这个bucket
STORAGE_BUCKET_NAME = 'media'
# ref: https://docs.djangoproject.com/en/dev/topics/files/




ADMINS = (
    ('administrator', 'zaibuo@126.com'),
)

# ref: https://docs.djangoproject.com/en/dev/ref/settings/#email
EMAIL_BACKEND = 'sae.ext.django.mail.backend.EmailBackend'
EMAIL_HOST = 'smtp.126.com'
EMAIL_PORT = 587
EMAIL_HOST_USER = 'sender@gmail.com'
EMAIL_HOST_PASSWORD = 'password'
EMAIL_USE_TLS = True
SERVER_EMAIL = DEFAULT_FROM_EMAIL = EMAIL_HOST_USER