from string import whitespace, punctuation

print("Подсчитаем слова в тексте")
user_list = {}
user_input = input("Введите слова: ").lower()
chars = '!#$%&\'()*+,-./:;<=>?@[\\]^_`{|}~'
for i in chars:
    user_input = user_input.replace(i, '')
if user_input.isspace() or user_input == "":
    print("Вы ввели пустую строку, завершаю программу")
    exit()
else:
    pass

for i in user_input.split():
    if i in user_list.keys():
        user_list[i] += 1
    else:
        user_list[i] = 1


def krasivii_dict(dict):
    print(f"{'Word':<30} {'Count':<30}")
    for k, v in dict.items():
        print(f'{k:<30} {v:<30}')


krasivii_dict(user_list)
