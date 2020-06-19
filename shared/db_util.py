import psycopg2


def db_conn():
    """Return just Conection to Database using psycopg2
    that allow cursor method"""

    connection_params = {'dbname': 'postgres',
                         'user': 'postgres',
                         'password': 'postgres',
                         'host': 'localhost',
                         'port': 5432}

    bdnet = psycopg2.connect(dbname=connection_params['dbname'],
                             user=connection_params['user'],
                             password=connection_params['password'],
                             host=connection_params['host'],
                             port=connection_params['port'])
    return bdnet
