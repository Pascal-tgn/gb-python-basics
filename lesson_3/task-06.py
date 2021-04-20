def int_func(text):
  return text.capitalize()

output = []

for word in input("Введите строку: ").split():
  output.append(int_func(word))

print(" ".join(output))