distance = float(input("Введите начальную дистанцию: "))
target   = float(input("Введите целевую дистанцию: "))

day = 1
print("{:>3}-й день: {:.3}".format(day, distance)) # некрасивенько


while target > distance:
  day += 1
  distance += distance / 10
  print("{:>3}-й день: {:.3}".format(day, distance))