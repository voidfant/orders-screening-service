from os import getenv
import requests
from dotenv import load_dotenv

import psycopg2 as psql
from python_shell import Shell




class PsqlActions:
    def __init__(self):
        load_dotenv(override=True)
        self.DB_NAME = getenv('DB_NAME')
        self.TABLE_NAME = getenv('TABLE_NAME')
        self.DEV_USER = getenv('DEV_USER')
        self.PROD_USER = getenv('PROD_USER')
        self.USERS_TABLE_NAME = getenv('USERS_TABLE_NAME')

    def initDatabase(self):
        Shell.createdb(self.DB_NAME)

        connection = psql.connect(dbname=self.DB_NAME, user=self.DEV_USER)
        cursor = connection.cursor()

        query1 = """
        CREATE TABLE {} (
            order_id bigserial primary key,
            order_number bigint NOT NULL,
            order_cost_usd integer NOT NULL,
            order_cost_rub integer NOT NULL,
            order_arrival varchar(10) NOT NULL
        );
        """.format(self.TABLE_NAME)

        query2 = """
        CREATE TABLE {} (
            user_id bigint NOT NULL,
            date_added varchar(10) NOT NULL
        );
        """.format(self.USERS_TABLE_NAME)

        cursor.execute(query1)
        cursor.execute(query2)
        connection.commit()
        cursor.close()
        connection.close()

    def insertData(self, data):
        connection = psql.connect(dbname=self.DB_NAME, user=self.DEV_USER)
        cursor = connection.cursor()
        rate = self.getUsdRate()
        for row in data:
            # if isOutdated(row[3]):
            #     notify()
            query = """INSERT INTO {} (order_number, order_cost_usd, order_cost_rub, order_arrival)
                        VALUES({},{},{},'{}')
                    """.format(self.TABLE_NAME, row[1], row[2], int(row[2]) * rate, row[3])
            cursor.execute(query)
        connection.commit()
        cursor.close()
        connection.close()

    def getAllUsers(self):
        connection = psql.connect(dbname=self.DB_NAME, user=self.DEV_USER)
        cursor = connection.cursor()
        query = "SELECT user_id FROM {};".format(self.USERS_TABLE_NAME)
        cursor.execute(query)
        result = cursor.fetchall()
        cursor.close()
        connection.close()

        return result

    def getAllArrivalDates(self):
        connection = psql.connect(dbname=self.DB_NAME, user=self.DEV_USER)
        cursor = connection.cursor()
        query = "SELECT order_number, order_arrival FROM {};".format(self.TABLE_NAME)
        cursor.execute(query)
        result = cursor.fetchall()
        cursor.close()
        connection.close()

        return result

    def clearTable(self):
        connection = psql.connect(dbname=self.DB_NAME, user=self.DEV_USER)
        cursor = connection.cursor()
        query = """DELETE FROM {} WHERE order_id != -1;
                   ALTER SEQUENCE {}_order_id_seq RESTART WITH 1;""".format(self.TABLE_NAME, self.TABLE_NAME)
        cursor.execute(query)
        connection.commit()
        cursor.close()
        connection.close()

    def downDatabase(self):
        Shell.dropdb(self.DB_NAME)

    def getUsdRate(self):
        data = requests.get('https://www.cbr-xml-daily.ru/daily_json.js').json()
        return int(data['Valute']['USD']['Value'])

    

    

if __name__ == '__main__':
    # print(PsqlActions().findOutdated('20.05.2022'))
    # print(PsqlActions().getAllUsers())
    print(PsqlActions().getAllArrivalDates())