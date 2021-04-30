f_in  = open("files/task-04-in.txt", "r")
f_out = open("files/task-04-out.txt", "w")

my_dict = {
  "1": "Один",
  "2": "Два",
  "3": "Три",
  "4": "Четыре"
}

for line in f_in:
  eng, _, k = line.split()
  f_out.write("{} - {}\n".format(my_dict[k], k))



f_in.close()
f_out.close()
