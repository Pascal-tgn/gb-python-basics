goods = []

while True:
  print("Введите информацию о товаре")
  name  = input("Название: ")
  if name == "quit":
    break
  price = int(input("Цена: "))
  qty   = int(input("Количество: "))
  unit  = input("Единица измерения: ")
  goods.append((len(goods) + 1, {"название": name, "цена": price, "количество": qty, "eд": unit}))

parameters = {}

for good in goods:
  for k, v in good[1].items():
    if k not in parameters:
      parameters[k] = []
    if v not in parameters[k]:
      parameters[k].append(v)

print(parameters)