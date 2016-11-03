from groupo.settings.common import *

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = False

ALLOWED_HOSTS = []

# Database
# https://docs.djangoproject.com/en/1.10/ref/settings/#databases

DATABASES = {
   'default': {
       'ENGINE': 'django.db.backends.postgresql_psycopg2',
       'NAME': 'Lonely_cat',
        'USER' : 'Master',
        'PASSWORD' : 'masterbeater',
       'HOST' : 'groupo-db1.csbt6xxcttnx.eu-west-1.rds.amazonaws.com',
       'PORT' : '5432',
   }
}
