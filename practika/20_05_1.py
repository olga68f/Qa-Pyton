
students = [
    {'name': "Alice", 'grades':[5,3,4,4]},
    {'name': "Bill", 'grades':[2,2,3]},
    {'name': "Bob", 'grades':[4,4,4,5]},
    {'name': "David", 'grades':[]}
    ]


def filter_students(st):
   
    filtred_students  = []
    for i in st:
        grades = i['grades']
        average_grade = sum(grades) / len(grades) if grades else 0
        if average_grade > 4:
            filtred_students.append(i['name'])
    return filtred_students


print(filter_students(students))




