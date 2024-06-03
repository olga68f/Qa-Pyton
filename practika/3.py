doxod = int(input())
reiting = int(input())
if doxod>=5000:
   print("доход выше 5000")
   if reiting >=7:
      print("кредит одобрен")
   else:
      print("рейтинг ниже 7,кредит не одобрен")
else:
   print("кредит не одобрен")
