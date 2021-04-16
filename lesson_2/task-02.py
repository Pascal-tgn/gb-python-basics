data = []

while True:
  el = input("Введите следующий элемент списка (quit для завершения): ")
  if el == "quit":
    break
  else:
    data.append(el)

limit = len(data) - 1 if (len(data) % 2 == 1) else len(data)

i = 0
while i < limit:
  data[i], data[i + 1] = data[i + 1], data[i]
  i += 2


print("Перевёрнутый массив: ", data)
