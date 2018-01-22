import os

from orator import DatabaseManager, Model


configurations = {
    'default': os.environ.get('DB_CONNECTION'),
    'mysql': {
        'driver': 'mysql',
        'host': os.environ.get('DB_HOST'),
        'port': os.environ.get('DB_PORT'),
        'database': os.environ.get('DB_DATABASE'),
        'user': os.environ.get('DB_USERNAME'),
        'password': os.environ.get('DB_PASSWORD'),
        'prefix': ''
    },
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

db = DatabaseManager(configurations)
Model.set_connection_resolver(db)
