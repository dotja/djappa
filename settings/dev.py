import os
from settings.common import *


DEBUG = True
ALLOWED_HOSTS = ['ip or domain']

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': os.getenv('DB_NAME'),
        'USER': os.getenv('DB_USER'),
        'PASSWORD': os.getenv('DB_PASSWORD'),
        'HOST': os.getenv('DB_HOST'),
        'PORT': os.getenv('DB_PORT'),
    }
}

AWS_STORAGE_BUCKET_NAME=os.getenv('AWS_STORAGE_BUCKET_NAME')
AWS_SECRET_ACCESS_KEY=os.getenv('AWS_SECRET_ACCESS_KEY')
AWS_ACCESS_KEY_ID=os.getenv('AWS_ACCESS_KEY_ID')
AWS_S3_CUSTOM_DOMAIN=os.getenv('AWS_S3_CUSTOM_DOMAIN')

STATIC_URL = 'https://your-bucket-and-region.amazonaws.com/'
STATICFILES_DIRS = [ os.path.join(BASE_DIR, 'static') ]
STATICFILES_STORAGE = 'storages.backends.s3boto3.S3Boto3Storage'


LOGIN_REDIRECT_URL = '/'
LOGOUT_REDIRECT_URL = '/'
