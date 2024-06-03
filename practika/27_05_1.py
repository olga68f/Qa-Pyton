import mysql.connector

try:
    config = {
        'host' : 'localhost',
        'user' : 'pucha68mai',
        'password': '111admin',
        'database': 'shop.sql'
    }
    print('successfully connected...')
except Exception as ex:
    print('connection refused')
    print(ex)
