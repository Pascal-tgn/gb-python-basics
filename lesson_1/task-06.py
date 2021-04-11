distance = float(input("Введите начальную дистанцию: "))
target   = int(input("Введите целевую дистанцию: "))

day = 1
print("{:>3}-й день: {:.3}".format(day, distance)) # некрасивенько


while target > distance:
  day += 1
  distance += distance / 10
  print("{:>3}-й день: {:.3}".format(day, distance))

print("Ответ: на {}-й день спортсмен достиг результата — не менее {} км.".format(day, target))