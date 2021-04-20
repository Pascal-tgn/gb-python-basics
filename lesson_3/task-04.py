def my_func_easy(x, y):
  print(x ** y)

def my_func(x, y):
  acc = x
  while y <= 0:
    acc /= x
    y += 1
  print(acc)

base  = int(input("Введите основание: "))
power = int(input("Введите степень: "))

if power >= 0:
  print("Степень должна быть меньше 0.")

my_func_easy(base, power)
my_func(base, power)