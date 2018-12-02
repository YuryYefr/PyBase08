a = input("Факториал числа ")
while a.isalpha():
    a = input("Введите число ")
factorial = 1
i = 0
while i < int(a):
     i += 1
     factorial = factorial * i
print("ваше число", factorial)