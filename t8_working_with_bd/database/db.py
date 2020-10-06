import pymysql.cursors
from t8_working_with_bd.utils.helpers import create_table


class DataBase:

    def __init__(self, host, user, password, database):
        self.host = host
        self.user = user
        self.password = password
        self.database = database
        self.db_connection = pymysql.connect(host=host,
                                             user=user,
                                             password=password,
                                             db=database,
                                             charset='utf8mb4',
                                             cursorclass=pymysql.cursors.DictCursor)
        self.db_cursor = self.db_connection.cursor()

    def close_connection(self):
        self.db_cursor.close()
        self.db_connection.close()

    def execute_query(self, query):
        self.db_cursor.execute(query)
        result = self.db_cursor.fetchall()
        create_table(result)





