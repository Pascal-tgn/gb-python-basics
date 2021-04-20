def my_func(a, b, c):
  arr = [a, b, c]
  arr.sort()
  return(arr[1] + arr[2])

numbers = []

for n in input("Введите 3 числа через пробел: ").split():
  numbers.append(int(n))

print(my_func(numbers[0], numbers[1], numbers[2]))
