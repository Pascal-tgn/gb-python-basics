def string_sum(string):
  numbers = string.split()
  stop = "q" in numbers
  total = 0
  for n in numbers:
    try:
      total += int(n)
    except:
      pass
  return total, stop

total = 0

while True:
  subtotal, stop = string_sum(input("Введите ряд чисел: "))
  total += subtotal
  print("Всего: {}".format(total))
  if stop:
    exit()
