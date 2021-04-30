import re

f = open("files/task-06.txt", "r")

tasks = {}

for line in f:
  subject = line.split()[0][0:-1]
  count = sum(map(int, re.findall(r'\d+' , line)))
  tasks[subject] = count

print(tasks)

f.close()