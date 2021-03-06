month = int(input("Введите номер месяца: "))

if 1 <= month <= 12:
  # Делаем через `list`

  month_to_season_list = [
    "Зима",  "Зима",
    "Весна", "Весна", "Весна",
    "Лето",  "Лето",  "Лето",
    "Осень", "Осень", "Осень",
    "Зима"
  ]
  print("{:>2}-й месяц -- это {}".format(month, month_to_season_list[month - 1]))

  # Делаем через `dict`
  
  month_to_season_dict = {
    1:  "Зима",  2:  "Зима",
    3:  "Весна", 4:  "Весна", 5:  "Весна",
    6:  "Лето",  7:  "Лето",  8:  "Лето",
    9:  "Осень", 10: "Осень", 11: "Осень",
    12: "Зима"
  }
  print("{:>2}-й месяц -- это {}".format(month, month_to_season_dict[month]))

else:
  print("Некорректный номер месяца")