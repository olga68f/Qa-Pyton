with open(r'C:\Users\AttekPC\Desktop\текст.txt', 'r') as file:
    search_word = 'Рэдрик'
    found_lines = []
   
    for line in file:
        if search_word in line:
            found_lines.append(line)
            print(found_lines)







