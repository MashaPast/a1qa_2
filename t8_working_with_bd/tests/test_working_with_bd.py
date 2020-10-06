from t8_working_with_bd.database.db import DataBase
from t8_working_with_bd.resources.config import config

db_config = config["DataBase"]
db_connection = DataBase(db_config['host'], db_config['user'], db_config['password'], db_config['db'])

q1 = "select p.name 'PROJECT', t.name 'TEST', t.end_time-t.start_time 'MIN_WORKING_TIME' from project p join test t " \
     "on p.id = t.project_id order by p.name, t.name ASC;"
q2 = "select p.name 'PROJECT', count(t.name) 'TESTS_COUNT' from project p join test t " \
     "on p.id= t.project_id group by p.id;"
q3 = "select p.name 'PROJECT', t.name 'TEST', t.start_time 'DATE' from project p join test t " \
     "on p.id = t.project_id where t.start_time > '20151108' order by p.name, t.name;"
q4 = "select count(*) 'BROWSERS' from test t where t.browser = 'chrome' union select count(*) from test t " \
     "where t.browser = 'firefox';"

db_connection.execute_query(q1)
db_connection.execute_query(q2)
db_connection.execute_query(q3)
db_connection.execute_query(q4)

db_connection.close_connection()

