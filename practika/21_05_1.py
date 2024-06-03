new_list = []
def chisla(my_list):
    for i in my_list:
        if i % 3 == 0:
            new_list.append(i)
    return(new_list)
print(chisla([10,20,21,23,27,36,42,43]))




