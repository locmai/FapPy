
def get_database(env_name):
    if env_name == 'development':
        return DEVELOPMENT_DATABASE
    if env_name == 'production':
        return PRODUCTION_DATABASE


def get_debug_mode(env_name):
    return env_name == 'development'


def get_allowed_hosts(env_name):
    if env_name == 'development':
        return ALLOWED_HOSTS_DEVELOPMENT
    if env_name == 'production':
        return ALLOWED_HOSTS_PRODUCTION



DEVELOPMENT_DATABASE = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'controlmdb',
        'USER': 'postgres',
        'PASSWORD': 'admin',
        'HOST': '127.0.0.1',
        'PORT': '5432',
    }
}

PRODUCTION_DATABASE = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': '',
        'USER': '',
        'PASSWORD': '',
        'HOST': '',
        'PORT': '',
    }
}

DEVELOPMENT_DEBUG = True
PRODUCTION_DEBUG = False

ALLOWED_HOSTS_DEVELOPMENT = ['localhost', '127.0.0.1']
# Heroku for example
ALLOWED_HOSTS_PRODUCTION = ['herokuapp.com']

SECRET_KEY = 'jpofekeb=r53gby=vam_j(i4w0$l&s0o03t!jhycn8$h8a8xk='