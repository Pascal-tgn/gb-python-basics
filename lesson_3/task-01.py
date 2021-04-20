def division(dividend, divisor):
  if divisor == 0:
    print("Делить на 0 не стоит.")
    exit()
  return dividend / divisor

dividend = float(input("Введите делимое: "))
divisor  = float(input("Введите делитель: "))

print(division(dividend, divisor))