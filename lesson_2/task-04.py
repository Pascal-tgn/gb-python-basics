line = input("Введите строку: ")

words = line.split()

for i, word in enumerate(words):
  if len(word) > 10:
    word = word[0:10]
  print("{:>2}-е слово: {}".format(i + 1, word))