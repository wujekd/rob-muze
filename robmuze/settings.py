"""
Django settings for robmuze project.

Generated by 'django-admin startproject' using Django 4.1.10.

For more information on this file, see
https://docs.djangoproject.com/en/4.1/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/4.1/ref/settings/
"""

from pathlib import Path
import os


# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/4.1/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-k@=ufwuq_glqqx9v__@kbm!_^a2jwk(p(r3u*3#fi0&$8tld$z'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ['*']
LOGIN_URL ='/login/'
LOGIN_REDIRECT_URL = '/'
LOGOUT_REDIRECT_URL = '/'


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'tailwind',
    'theme',
    'django_browser_reload',
    # 'social_django',
    'django_recaptcha',
    # 'captcha',
    'core',
    'samples',
    'account',
    'ankiety',
    'collabs',
    'ideas',
    'groups',
]

TAILWIND_APP_NAME = 'theme'
INTERNAL_IPS = [
    "127.0.0.1",
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.locale.LocaleMiddleware',
    # 'path.to.ForceDefaultLanguageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'social_django.middleware.SocialAuthExceptionMiddleware',
    "django_browser_reload.middleware.BrowserReloadMiddleware",
    
]

ROOT_URLCONF = 'robmuze.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [ BASE_DIR / 'robmuze/templates'],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
                
                'robmuze.context_processors.unanswered_polls',
                'robmuze.context_processors.downloadCounter',
                'robmuze.context_processors.user_points',
                
                'social_django.context_processors.backends',
                'social_django.context_processors.login_redirect',
            ],
        },
    },
]

WSGI_APPLICATION = 'robmuze.wsgi.application'


# Database
# https://docs.djangoproject.com/en/4.1/ref/settings/#databases

# DATABASES = {
#     'default': {
#         'ENGINE': 'django.db.backends.sqlite3',
#         'NAME': BASE_DIR / 'db.sqlite3',
#     }
# }

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'tesdb',
        'USER': 'dw',
        'PASSWORD': 'admin',
        'HOST': 'localhost',
        'PORT': '5432',
    }}


AUTHENTICATION_BACKENDS = (
    'social_core.backends.facebook.FacebookOAuth2',

    'django.contrib.auth.backends.ModelBackend',
)


RECAPTCHA_PUBLIC_KEY = '6Lcl89kpAAAAABnTwh9k2Hpv2cAxmxrQNKgpx52f'
RECAPTCHA_PRIVATE_KEY = '6Lcl89kpAAAAAMTJCZcoAvV3o_OaAEVwkOKKKENa'
SILENCED_SYSTEM_CHECKS = ['captcha.recaptcha_test_key_error']

# Password validation
# https://docs.djangoproject.com/en/4.1/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/4.1/topics/i18n/

LANGUAGE_CODE = 'pl'

LANGUAGES = [
    ('en', 'English'),
    ('pl', 'Polish'),
]

TIME_ZONE = 'UTC'

USE_I18N = True

USE_TZ = True

LOCALE_PATHS = [
    os.path.join(BASE_DIR , 'locale')
]


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.1/howto/static-files/

STATIC_URL = 'static/'
# STATICFILES_DIRS = [ BASE_DIR / 'static']
import os

STATIC_URL = '/static/'
STATICFILES_DIRS = [ BASE_DIR / 'static']

# STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')

MEDIA_URL = '/media/'
MEDIA_ROOT = BASE_DIR / 'media'


EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_HOST_USER = 'robmuzepl@gmail.com'
EMAIL_HOST_PASSWORD = 'ssfwklypjrtoxeux'
EMAIL_PORT = 587
EMAIL_USE_TLS = True
EMAIL_USE_SSL = False

PASSWORD_RESET_TIMEOUT = 14400


# Default primary key field type
# https://docs.djangoproject.com/en/4.1/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

