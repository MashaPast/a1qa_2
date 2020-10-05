import pymysql.cursors
from t8_working_with_bd.utils.helpers import create_table


class DataBase:
    def __init__(self):
        self.db_connection = pymysql.connect(host='localhost',
                                             user='root',
                                             password='ri4ards',
                                             db='union_reporting',
                                             charset='utf8mb4',
                                             cursorclass=pymysql.cursors.DictCursor)
        self.db_cursor = self.db_connection.cursor()

    def close_connection(self):
        self.db_cursor.close()
        self.db_connection.close()

    def select_project_test_and_min_working_time(self):
        self.db_cursor.execute("select p.name 'PROJECT', t.name 'TEST', t.end_time-t.start_time 'MIN_WORKING_TIME' "
                               "from project p join test t on p.id = t.project_id order by p.name, t.name ASC;")
        result = self.db_cursor.fetchall()
        create_table(result)
        self.db_connection.commit()

    def select_projects_with_unique_tests(self):
        self.db_cursor.execute("select p.name 'PROJECT', count(t.name) 'TESTS_COUNT' from project p join test t on p.id"
                               "= t.project_id group by p.id;")
        result = self.db_cursor.fetchall()
        create_table(result)
        self.db_connection.commit()

    def select_projects_with_tests_after_20151108(self):
        self.db_cursor.execute("select p.name 'PROJECT', t.name 'TEST', t.start_time 'DATE' from project p join test t "
                               "on p.id = t.project_id where t.start_time > '20151108' order by p.name, t.name;")
        result = self.db_cursor.fetchall()
        create_table(result)
        self.db_connection.commit()

    def select_num_of_browser_tests(self):
        self.db_cursor.execute("select count(*) 'BROWSERS' from test t where t.browser = 'chrome' union select count(*)"
                               "from test t where t.browser = 'firefox';")
        result = self.db_cursor.fetchall()
        create_table(result)
        self.db_connection.commit()


db = DataBase()
db.select_project_test_and_min_working_time()
db.select_projects_with_unique_tests()
db.select_projects_with_tests_after_20151108()
db.select_num_of_browser_tests()
db.close_connection()
