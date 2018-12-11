from string import whitespace, punctuation

user_input1 = input("Введите слова").lower()
if user_input1.isspace():
    print("Вы ввели пустую строку, завершаю программу")
    exit()
else:
    pass
user_input1 = user_input1.split()
for element in user_input1:
    if user_input1.count(element) > 1:
        user_input1.remove(element)
user_input1.sort()
print(user_input1)
