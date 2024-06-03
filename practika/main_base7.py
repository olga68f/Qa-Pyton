import pymysql
import pymysql.cursors
from main_config_base import host,user,password,db_name


try:
    connection = pymysql.connect(
    host=host,
    port=3306,
    user=user,
    password=password,
    database=db_name,
    cursorclass=pymysql.cursors.DictCursor
    )
    print('succsess')
    print('#' * 30)
    try:
        with connection.cursor() as cursor:
            #создал таблицу
            create_table_query = '''
            CREATE TABLE IF NOT EXISTS `team`(
            id INT AUTO_INCREMENT PRIMARY KEY,
            name_team VARCHAR(255) NOT NULL,
            
            person INT (10)
            );
            '''
            cursor.execute(create_table_query)
            print('table team created')


            #заполняю таблицу
            insert_query = '''
            INSERT INTO `team` (name_team,person) VALUES
            
            
            (' Erik',10),
            ('jon ',1),
            ( "jona",2),
            ('joner Erik',3),
            ("tanya",4),
            ("olga",5),
            ("sergei",6),
            ("ivan",7),
            ("sasha",8),
            ("masha",9);
            '''
            cursor.execute(insert_query)
            connection.commit()
            print('data inserted')

            
            q = """ SELECT * FROM team WHERE person>5 """
            cursor.execute(q)
            rows = cursor.fetchall()
            if rows:
                print("Команды с количеством участников более 5:")
                for row in rows:
                    print(row)
            else:
                print('отсутствуют команды с количеством участников менее 5')






    except Exception as e:
        print('An error ')
        print(e)        
           
    finally:
        connection.close()
except Exception as ex:
    print('Connection rufus')
    print(ex)




