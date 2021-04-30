f = open("files/task-02.txt", "r")

lines = f.readlines()

print("В файле {} строк".format(len(lines)))

i = 1
for line in lines:
  print("В {}-й сроке -- {} слов".format(i, len(line.split())))
  i += 1

f.close()