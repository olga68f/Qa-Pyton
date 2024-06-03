
import random


joke_templates = [
    'Почему %s катится вниз?',
    'Потому что %s смеятся над ним!',
    'Кто %s в книгах?',
    'Кто %s?',
    'Что сказал %s ему %s когда %s они %s встретились ?'
]
joke_elements = [
    'слон','заяц','бетмен','крокодил','чебурашка','студент','препод',
    'водитель','улитка'
]


joke_template = random.choice(joke_templates)


joke = joke_template % random.choice(joke_elements)
print(joke)


