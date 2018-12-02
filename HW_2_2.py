# Сумма натуральных чисел
a = input("Введите число")
while a.isalpha():
    a = input("Введите число")
b = input("Введите число:")
while b.isalpha():
    b = input("Введите число")
Some_list = 0
for i in range(int(a), int(b) + 1):
    Some_list += i
print(Some_list)

