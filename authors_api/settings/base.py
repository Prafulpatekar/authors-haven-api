from pathlib import Path
import environ

# from authors_api.settings import INSTALLED_APPS

env = environ.Env()

# To make ROOT_DIR as same location like manange.py here
ROOT_DIR = Path(__file__).resolve().parent.parent.parent


APPS_DIR = ROOT_DIR / "core_apps"



# Going to be read from enviroment variable 
#if this DJANGO_DEBUG doesn't exists the by default it is False
DEBUG = env.bool("DJANGO_DEBUG",False) 




# DJANGO Application definition
DJANGO_APPS = [
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.sites',# add this by myself
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.admin',
]
# Application definition
THIRD_PARTY_APPS = [
    'rest_framework',# pip install djangorestframework
    'django_filters',# pip install django-filters
    'django_countries',
    'phonenumber_field',
    'drf_yasg',
    'corsheaders',
]

# Application definition
LOCAL_APPS = [
    "core_apps.common",
    "core_apps.users",
    "core_apps.profiles",
]

INSTALLED_APPS = DJANGO_APPS + THIRD_PARTY_APPS + LOCAL_APPS

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'corsheaders.middleware.CorsMiddleware',# add cors middelware for cors policy
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.common.BrokenLinkEmailsMiddleware',# for any broken email link
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'authors_api.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [str(APPS_DIR / "templates")],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.template.context_processors.i18n',# for translation
                'django.template.context_processors.static',# for static files
                'django.template.context_processors.tz',# for timezone
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'authors_api.wsgi.application'


# Database
# https://docs.djangoproject.com/en/4.1/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': ROOT_DIR / 'db.sqlite3',
    }
}

# DATABASES = {
#     'default': env.db("DATABASE_URL")
# }

DATABASES["default"]["ATOMIC_REQUESTS"] = True
"""
It works like this. Before calling a view function, 
Django starts a transaction. 
If the response is produced without problems, 
Django commits the transaction.
If the view produces an exception, 
Django rolls back the transaction.
"""
# Read more about password hashers
PASSWORD_HASHERS = [
    'django.contrib.auth.hashers.Argon2PasswordHasher',
    'django.contrib.auth.hashers.PBKDF2PasswordHasher',
    'django.contrib.auth.hashers.PBKDF2SHA1PasswordHasher',
    'django.contrib.auth.hashers.BCryptSHA256PasswordHasher',
    # 'django.contrib.auth.hashers.ScryptPasswordHasher', # we are not going to use this
]

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

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'Asia/Kolkata'

USE_I18N = True

USE_TZ = True

SITE_ID = 1 # beacause we added django.contrib.sites in DJANGO_APP List we has to specify a SITE_ID

ADMIN_URL = "supersecret/"# can make this whatever i want

ADMINS = [("""Praful Coder""","prafulpatekar23@gmail.com")] 

MANAGERS = ADMINS




# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.1/howto/static-files/

STATIC_URL = '/staticfiles/'
STATIC_ROOT = str(ROOT_DIR / 'staticfiles' )
STATICFILES_DIRS = []
STATICFILES_FINDERS = [
    'django.contrib.staticfiles.finders.FileSystemFinder',
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
]

MEIDA_URL = '/mediafiles/'
MEDIA_ROOT = str(ROOT_DIR / 'mediafiles' )



# Default primary key field type
# https://docs.djangoproject.com/en/4.1/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

CORS_URLS_REGEX = r"^/api/.*$"
# only allow this origin

LOGGING = {
    "version": 1,
    "disable_existing_loggers":False,
    "formatters":{
        "verbose":{
            "format":"%(levelname)s %(name)-12s %(asctime)s %(module)s " "%(process)d %(thread)d %(message)s"
        }
    },
    "handlers":{
        "console":{
            "level":"DEBUG",
            "class":"logging.StreamHandler",
            "formatter":"verbose",
        }        

    },
    "root":{"level":"INFO","handlers":["console"]},

}

# LOGGING = {
#     'version': 1,
#     'disable_existing_loggers': False,
#     'handlers': {
#         'console': {
#             'class': 'logging.StreamHandler',
#         },
#     },
#     'root': {
#         'handlers': ['console'],
#         'level': 'WARNING',
#     },
# }