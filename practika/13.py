def check_password(password):
    if len(password) <8:
        return False
   
   
   

print(check_password('Abcd1234')) #True
print(check_password('qwerty')) #False
print(check_password('abcD')) #False
print(check_password('ABCD1234')) #False

