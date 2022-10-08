from os import getenv
from dotenv import load_dotenv
import psycopg2 as psql
from datetime import date


class PsqlActions:
    def __init__(self):
        load_dotenv(override=True)
        self.DB_NAME = getenv('DB_NAME')
        self.TABLE_NAME = getenv('TABLE_NAME')
        self.DEV_USER = getenv('DEV_USER')
        self.PROD_USER = getenv('PROD_USER')
        self.USERS_TABLE_NAME = getenv('USERS_TABLE_NAME')

    def addUserToMailingList(self, user_id):
        connection = psql.connect(dbname=self.DB_NAME, user=self.DEV_USER)
        cursor = connection.cursor()
        query = """INSERT INTO {} (user_id, date_added) VALUES('{}', '{}')""".format(self.USERS_TABLE_NAME, user_id, str(date.today()))
        cursor.execute(query)
        connection.commit()
        cursor.close()
        connection.close()

    def findUserInMailingList(self, user_id):
        connection = psql.connect(dbname=self.DB_NAME, user=self.DEV_USER)
        cursor = connection.cursor()
        query = "SELECT user_id FROM {} WHERE user_id='{}'".format(self.USERS_TABLE_NAME, user_id)
        cursor.execute(query)
        
        return cursor.fetchone()

    def removeUserFromMailingList(self, user_id):
        connection = psql.connect(dbname=self.DB_NAME, user=self.DEV_USER)
        cursor = connection.cursor()
        query = "DELETE FROM {} WHERE user_id = '{}'".format(self.USERS_TABLE_NAME, user_id)
        cursor.execute(query)
        connection.commit()
        cursor.close()
        connection.close()