def user_info(first_name, last_name, birth_year, city, email, phone):
  print(", ".join([first_name, last_name, birth_year, city, email, phone]))

first_name = input("Введите имя: ")
last_name  = input("Введите фамилию: ")
birth_year = input("Введите год рождения: ")
city       = input("Введите город: ")
email      = input("Введите e-mail: ")
phone      = input("Введите телефон: ")

user_info(first_name=first_name, last_name=last_name, birth_year=birth_year, city=city, email=email, phone=phone)