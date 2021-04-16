ratings = [9, 7, 5, 3, 1]

while True:
  rating = int(input("Введите элемент: "))
  if rating > 0:
    for k, v in enumerate(ratings):
      if v < rating or k == len(ratings) - 1:
        ratings.insert(k, rating)
        print(ratings)
        break