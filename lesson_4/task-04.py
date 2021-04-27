def uniques():
  my_list = [2, 2, 2, 7, 23, 1, 44, 44, 3, 2, 10, 7, 4, 11]
  for n in range(0, len(my_list)):
    if my_list.count(my_list[n]) == 1:
      yield my_list[n]

print(list(uniques()))