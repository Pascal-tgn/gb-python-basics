from random import randrange

f = open("files/task-05.txt", "w+")

COUNT = 100

i = 0

print("*" * 10, " Пишем файл  ", "*" * 10)

while i < COUNT:
  i += 1
  f.write(str(randrange(0, 100)))
  f.write(" ")

f.seek(0)

print("*" * 10, " Читаем файл ", "*" * 10)

sum = 0

for i in f.read().split():
  sum += int(i)

print("Сумма записанных в файл чисел: {}".format(sum))

f.close()