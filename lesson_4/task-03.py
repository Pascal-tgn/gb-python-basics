def my_gen():
  for i in range(20,240):
    if i % 20 == 0 or i % 21 == 0:
      yield i

print(list(my_gen()))