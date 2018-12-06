# Сумма натуральных чисел
a = input("Введите натуральное число")
while a.isalpha() or int(a) < 0:
    a = input("Введите натуральное число")
b = input("Введите натуральное число, значение которого выше введенного вами ранее:")
while b.isalpha() or int(b) < 0 or int(b) <= int(a):
    b = input("Введите натуральное число")
Some_list = 0
for i in range(int(a), int(b) + 1):
    Some_list += i
print("Сейчас произойдет сумма всех натуральных чисел в диапазоне введенных")
print(Some_list)

