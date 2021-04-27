from itertools import count, cycle

n = int(input("Введите начальное число: "))

for i in count(n):
  if i > n + 10:
    break
  print(i)

my_list = ["foo", "bar", "baz", "quux"]
i = 0

for s in cycle(my_list):
  if i > 10:
    break
  print(s)
  i += 1