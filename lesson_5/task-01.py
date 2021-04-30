f = open("files/task-01.txt", "w")

while True:
  line = input("Следующая строка: ")
  if line == "":
    break
  f.write(line + "\n")

f.close()