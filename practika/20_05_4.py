
def valid_num(num):
    if len(num) != 12 or num[0] != "+":
        return False
   
    for i in num[1:]:
        if not i.isdigit():
            return False
    return True


print(valid_num('+79956247294'))
print(valid_num('79956247294'))
print(valid_num('+7995624'))
print(valid_num('+asdjsadhsua'))

