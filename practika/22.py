with open(r'C:\Users\AttekPC\Desktop\текст.txt', 'r') as file:lines = file.readlines() 


for i in range(1,len(lines),2):
        print(lines[i])
