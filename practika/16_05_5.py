import re


user_database = {
    "user1@example.com": {'name':'User', 'password': 'Qwe12343r'},
    "user2@example.com": {'name':'Vasya', 'password': 'Qwe12343r'},
    "user3@example.com": {'name':'Petya', 'password': 'Qwe12343r'},
    "user4@example.com": {'name':'Sereja', 'password': 'Qwe12343r'},
}






def reg_user():
    while True:
        name = input('введи имя:')
        email = input('Введи почту: ')
        password = input('введи пароль: ')




        #проверка корректности имени
        if not re.match(r'[a-zA-Z-]',name):
            print('Недопустимое имя')
            continue


        if len(name) <2:
            print('короткий имя')
            continue


        if not re.match(r'^[a-zA-Z0-9._-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$', email):
            print('недопустимая почта!')
            continue
        if len(password) < 8:
            print('короткий')
            continue
        if not any(char.isupper() for char in password):
            print('должен иметь хоть 1 заглавную')
            continue
        if not any(char.islower() for char in password):
            print('должен быть хотя бы 1 мелкий буква')
            continue
        if not any(char.isdigit() for char in password):
            print('Цифру вбей хоть 1')
            continue
        if not any(char in '!@#$%^&*()-_=+[{]};;\",<>/>`~' for char in password):
            print('в пароле символа нет')
            continue
        if email in user_database:
            print('такой уже есть')
            continue


        user_database[email] = {'name': name, 'password': password}


        print('новый чувак создан')
        view_database = input('смотрим базу? y/n')
        if view_database.lower() == 'y':
            print(user_database)
            break
reg_user()





