"""
Django settings for mysite project.

Generated by 'django-admin startproject' using Django 1.10.4.

For more information on this file, see
https://docs.djangoproject.com/en/1.10/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.10/ref/settings/
"""

import os

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.10/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '^2c-h@c6&)clx908%ir7inhj#7)0=y@885k%$tna=rr^xnxle('

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ['*']


# Application definition

INSTALLED_APPS = [
    'app1.apps.App1Config',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
]

MIDDLEWARE = [
    'django.middleware.locale.LocaleMiddleware',
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

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
# https://docs.djangoproject.com/en/1.10/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}


# Password validation
# https://docs.djangoproject.com/en/1.10/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/1.10/topics/i18n/

LANGUAGE_CODE = 'en-us'
TIME_ZONE = 'UTC'
USE_I18N = True 
USE_L10N = True
USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.10/howto/static-files/

STATIC_URL = '/static/'
STATICFILES_DIRS = [
    os.path.join(BASE_DIR, "static"),
]

##
# application specific defs
##
jsondir=BASE_DIR+'/../../tmp/jsondir/'
logdir="/var/www/html/execjson/"
use_authorization=False # let this be True, if you want to use authorization feature
role_opsusers=['user1']
role_applusers=['user2']
use_workflow=False # let this be True, if you want to use workflow feature
role_managers=['user9']
use_svg_form=False # If True, template will be use svg feature in its HTML form
jobs=[
 {'jobname': 'mkdir',
  'args': ["server", "path", "owner", "group", "mode"]
 },
 {'jobname': 'filetransfer',
  'args': ["srcserver", "srcpath", "dstserver", "dstpath", "owner", "group", "mode"]
 },
 {'jobname': "deletefile",
  "args": ["server", "filepath"]
 },
 {'jobname': "execshell",
  "args": ["server", "path", "user", "background"]
 },
 {'jobname': "editcron",
  "args": ["operation", "server", "user", "minute", "hour", "day", "month", "dayofweek", "command"]
 },
 {'jobname': "editat",
  "args": ["operation", "server", "user", "minute", "hour", "day", "month", "year", "command"]
 },
 {'jobname': "mountnfs",
  "args": ["operation", "servername", "mountpoint", "mountoption", "nfsserver", "exportpath"]
 },
 {'jobname': "execsql",
  "args": ["operation", "dbname", "filename"]
 },
 {'jobname': "modifyuseros",
  "args": ["operation", "server", "username", "firstname", "lastname" ,"groups"]
 },
 {'jobname': "passwdresetos",
  "args": ["server", "username"]
 },
 {'jobname': "modifydns",
  "args": ["operation", "fqdn", "ipaddr"]
 },
 {'jobname': "addfirewallpolicy",
  "args": ["srcaddress", "srcnetmask", "destaddress", "destnetmask", "applicationname", "policy_then"]
 }
]
operationswithseveralops=['mkdir','filetransfer','editcron','editat', 
 'modifyuseros', 'passwdresetos', 'deletefile', "modifydns"
]
