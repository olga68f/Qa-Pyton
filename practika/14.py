word = input("введи слово ")
my_dict = {}

for i in word:
    if i in my_dict:
        my_dict[i] +=1
    else:
        my_dict[i] = 1
print(my_dict)

