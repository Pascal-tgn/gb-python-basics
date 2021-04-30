f = open("files/task-03.txt", "r")

less_than_20k = []
sum = 0
count = 0

for line in f:
  last_name, salary = line.split()
  salary = float(salary)
  if salary <= 20000:
    less_than_20k.append(last_name)
  sum += salary
  count += 1

print("Зарплата меньше 20000 у следующих сотрудников: {}".format(", ".join(less_than_20k)))
print("Средняя зарплата -- {}".format(round(sum / count, 2)))

f.close()

