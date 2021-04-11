total_seconds = int(input("Введите количество секунд: "))

total_minutes, seconds = divmod(total_seconds, 60)
hours, minutes = divmod(total_minutes, 60)

print("{}:{:0>2}:{:0>2}".format(hours, minutes, seconds))
