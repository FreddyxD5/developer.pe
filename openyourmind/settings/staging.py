from .base import *


DEBUG = False
ALLOWED_HOSTS = ['developerpe.herokuapp.com','.developerpe.com']

# Database
# https://docs.djangoproject.com/en/1.10/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'd5ito1oosb5vim',
        'USER': 'zrptgxzpejanfu',
        'PASSWORD': 'c6eae4c0142b34ba368c50c6885ef4744f9d4063b954b19e877e2296205a4b7d',
        'HOST': 'ec2-107-21-201-57.compute-1.amazonaws.com',
        'PORT': '5432',
    }
}
import dj_database_url
db_from_env = dj_database_url.config()
DATABASES['default'].update(db_from_env)
DATABASES['default']['CONN_MAX_AGE'] = 500

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.10/howto/static-files/

STATIC_URL = '/static/'
AUTH_USER_MODEL = 'usuarios.User'

MEDIA_URL = '/media/'
STATIC_ROOT = os.path.join(os.path.dirname(BASE_DIR), 'staticfiles')
STATICFILES_DIRS=[
	os.path.join(os.path.dirname(BASE_DIR),'static'),
		]

LOGIN_REDIRECT_URL= reverse_lazy('post:index')
LOGOUT_REDIRECT_URL= reverse_lazy('login')
