proceeds = int(input("Введите сумму выручки: "))
expenses = int(input("Введите сумму издержек: "))

if proceeds > expenses:
  print("У нас прибыль,", proceeds - expenses)
  print("Рентабельность --", (proceeds - expenses) / proceeds)
  employees = int(input("Введите количество сотрудников: "))
  print("Прибыль на каждого сотрудника равна", (proceeds - expenses) / employees)
elif proceeds == expenses:
  print("Вышли в ноль")
else:
  print("Работаем в убыток,", expenses - proceeds)