import pprint
from string import whitespace, punctuation

print("Подсчитаем слова в тексте")
user_list = {}
user_input = input("Введите слова: ").lower()
if user_input.isspace():
    print("Вы ввели пустую строку, завершаю программу")
    exit()
else:
    pass

for i in user_input.split():
    if i in user_list.keys():
        user_list[i] += 1
    else:
        user_list[i] = 1
pprint.pprint(user_list)
