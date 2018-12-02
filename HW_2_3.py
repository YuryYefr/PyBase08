#Факториал
a = input("Факториал числа ")
while a.isalpha() or int(a) < 0:
    a = input("Введите целое число ")
factorial = 1
i = 0
while i < int(a):
     i += 1
     factorial = factorial * i
print("ваше число", factorial)
