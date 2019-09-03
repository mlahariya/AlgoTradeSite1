import os
import warnings
from django.utils.translation import ugettext_lazy as _
from os.path import dirname

warnings.simplefilter('error', DeprecationWarning)

BASE_DIR = dirname(dirname(os.path.abspath(__file__)))
print(BASE_DIR)
CONTENT_DIR = os.path.join(BASE_DIR, 'content')
print(CONTENT_DIR)

SECRET_KEY = 'NhfTvayqggTBPswCXXhWaN69HuglgZIkM'

DEBUG = True
ALLOWED_HOSTS = ['*']

SITE_ID = 1

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.sites',

    # vendor --- its a package we use to Costomize our website
    "bootstrap4",
    
    # Application apps
    'main',
    'accounts',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.locale.LocaleMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'mysite2.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [
            os.path.join(CONTENT_DIR, 'templates'),
        ],
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

WSGI_APPLICATION = 'mysite2.wsgi.application'


# email to be sent to places from here. we can register our email host from here.
EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = "smtp.gmail.com"
EMAIL_USE_TLS = True
EMAIL_PORT = 587
EMAIL_FILE_PATH = os.path.join(CONTENT_DIR, 'tmp/emails')
EMAIL_HOST_USER = 'eruditelabs@gmail.com'
DEFAULT_FROM_EMAIL = 'eruditelabs@gmail.com'
# these are 2 step verification app passwords
EMAIL_HOST_PASSWORD = 'kczimlithravqfzg'
EMAIL_DEFAULT_PASSWORD = 'kczimlithravqfzg'








DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}

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



# properties of opening an account

ENABLE_USER_ACTIVATION = True
DISABLE_USERNAME = False
LOGIN_VIA_EMAIL = False
LOGIN_VIA_EMAIL_OR_USERNAME = True
LOGIN_REDIRECT_URL = '/'
LOGIN_URL = 'accounts:log_in'
USE_REMEMBER_ME = True

RESTORE_PASSWORD_VIA_EMAIL_OR_USERNAME = False
ENABLE_ACTIVATION_AFTER_EMAIL_CHANGE = True

SIGN_UP_FIELDS = ['username', 'first_name', 'last_name', 'email', 'password1', 'password2']
if DISABLE_USERNAME:
    SIGN_UP_FIELDS = ['first_name', 'last_name', 'email', 'password1', 'password2']

MESSAGE_STORAGE = 'django.contrib.messages.storage.cookie.CookieStorage'

USE_I18N = True
USE_L10N = True
LANGUAGE_CODE = 'en'
LANGUAGES = [
    ('en', _('English')),
    ('ru', _('Russian')),
    ('zh-Hans', _('Simplified Chinese')),
]

TIME_ZONE = 'UTC'
USE_TZ = True


# Static files contain our JSS and CS files. There are saved in static file dir, and when we run collectstatic from
# manage.py, they are copied to a static dir. this is the place - static root. now these static root files will be
# referenced in html codes.
# collectstatic has to be run every time we update anything in js or css before running the server.

# where static files are stored after collectstatic is run
STATIC_ROOT = os.path.join(CONTENT_DIR, 'static')
STATIC_URL = '/static/'
print(STATIC_ROOT)

MEDIA_ROOT = os.path.join(CONTENT_DIR, 'media')
MEDIA_URL = '/media/'

# where the app also searchs for additional static files. from here, collect static copies static files.
STATICFILES_DIRS = [
    os.path.join(CONTENT_DIR, 'assets'),
]

LOCALE_PATHS = [
    os.path.join(CONTENT_DIR, 'locale')
]


# IMAGES
# to add images from unsplash or any other website, we need to pull the api url. NOT JUST THE IMG LINK. this has to
# be copied in the assets (staticfiles_dir) folder, before making the collectstatic call. Otherwise the image will
# not be downloaded

