from string import whitespace, punctuation

user_input1 = input("Введите слова").lower()
chars = '!#$%&\'()*+,-./:;<=>?@[\\]^_`{|}~'
for i in chars:
    user_input1 = user_input1.replace(i, '')

if user_input1.isspace() or user_input1 == "":
    print("Вы ввели пустую строку, завершаю программу")
    exit()
else:
    pass
user_input1 = user_input1.split()
for element in user_input1:
    if user_input1.count(element) > 1:
        user_input1.remove(element)


def krasivii_dict(dict):
    print(f"{'Word':<30} {'Count':<30}")
    for k, v in dict.items():
        print(f'{k:<30} {v:<30}')


user_input1.sort()
print(user_input1)
