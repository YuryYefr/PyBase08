import pprint
from string import whitespace, punctuation

user_input1 = input("Введите слова").lower()
if user_input1.isspace():
    print("Вы ввели пустую строку, завершаю программу")
    exit()
else:
    user_input1 = user_input1.split()
    user_input1.sort()
    print(user_input1)
