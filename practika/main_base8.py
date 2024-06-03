import pymysql
import pymysql.cursors
from maim_confing_base import host, user, password, db_name

try:
    connection = pymysql.connect(
    host=host,
    port=3306,
    user=user,
    password=password,
    database=db_name,
    cursorclass=pymysql.cursors.DictCursor
    )
    print('OK')
    print('#'*30)
    try:
        with connection.cursor() as cursor:
            




            CREATE_good = '''CREATE VIEW user_A_B_2018 AS SELECT * FROM user WHERE YEAR(reg_date) = 2018 AND name LIKE "A%" OR name LIKE "Б%" OR name LIKE "% А%" OR name LIKE "% Б%"; '''

            cursor.execute(CREATE_good)
 
    finally:
        connection.close()
except Exception as ex:
    print('Connection rufus')
    print(ex)
