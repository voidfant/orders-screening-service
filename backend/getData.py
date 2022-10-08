import psycopg2 as psql
from buildJson import build
from os import getenv
from dotenv import load_dotenv

def pullData(internal: bool):
    load_dotenv()

    DB_NAME = getenv('DB_NAME')
    TABLE_NAME = getenv('TABLE_NAME')
    DEV_USER = getenv('DEV_USER')

    connection = psql.connect(dbname=DB_NAME, user=DEV_USER)
    cursor = connection.cursor()
    query = 'SELECT * FROM {};'.format(TABLE_NAME)
    cursor.execute(query)
    rs = cursor.fetchall()
    cursor.close()
    connection.close()
    
    return build(data=rs, internal=internal)

def countProfit():
    load_dotenv()

    DB_NAME = getenv('DB_NAME')
    TABLE_NAME = getenv('TABLE_NAME')
    DEV_USER = getenv('DEV_USER')

    profit = 0
    
    connection = psql.connect(dbname=DB_NAME, user=DEV_USER)
    cursor = connection.cursor()
    query = 'SELECT order_cost_usd FROM {};'.format(TABLE_NAME)
    cursor.execute(query)
    rs = cursor.fetchall()
    cursor.close()
    connection.close()

    for v in rs:
        profit += v[0]
    
    return profit

