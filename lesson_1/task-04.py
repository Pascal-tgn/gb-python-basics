number = int(input("Введите целое положительное число: "))

if number < 0:
  print("Введённое число меньше нуля")
  exit()

max = 0

while True:
  number, digit = divmod(number, 10)
  if digit > max:
    max = digit
  if number == 0:
    break

print("Самая большая цифра равна", max)