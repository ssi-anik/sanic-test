import os

from dotenv import load_dotenv
from os.path import join, dirname

dotenv_path = join(dirname('__file__'), '.env')
load_dotenv(dotenv_path)

DATABASES = {
    'postgres': {
        'driver': 'postgres',
        'host': os.environ.get('DB_HOST'),
        'port': os.environ.get('DB_PORT'),
        'database': os.environ.get('DB_DATABASE'),
        'user': os.environ.get('DB_USERNAME'),
        'password': os.environ.get('DB_PASSWORD'),
        'prefix': ''
    }
}
