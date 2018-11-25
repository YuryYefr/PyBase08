#Запрос имени и фамилии пользователя
name = input("what is your name?: ").title()
surname = input("what is your surname?:").title()
print(f"Hello {name} {surname}!")
#Дата рождения
year = int(input("what year you were born?: "))
day = int(input("day: "))
month = int(input("month:  "))
user_input_y = 2018 - year
user_input_m = user_input_y * 12 + (11 - month)
user_input_d = 349 - ((month - 1) * 30 + day) + user_input_y * 360
print(f"You are {user_input_y} years old or {user_input_m} months old")
#Прожито до начала курса 19.11.2018
print(f"you lived before course start {user_input_d} days, {user_input_m} months, {user_input_y} years!")



