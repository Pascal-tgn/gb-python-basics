from sys import argv
try:
  hours, salary, bonus = argv[1:4]
  payment = int(hours) * int(salary) + int(bonus)
  print("Зарплата равна", payment)
except:
  print("Использование: {} часы ставка премия".format(argv[0]))