def find_word():
    import re
    text =input('"введи слова": ')



    word=input('какое слово ты хочешь найти? ')
    words = re.sub(r'[^\w\s]', '', text)
    if word in words:
        return print(word, 'слово найдено')
    else:
        return print(word,'слово отсутствует в заданной строку')
find_word()