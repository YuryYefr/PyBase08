#Уравнение
import math
a = input("Введите число:")
while a.isalpha():
    a = input("Введите число")
b = input("Введите число:")
while b.isalpha():
    b = input("Введите число")
c = input("Введите число:")
while c.isalpha():
    c = input("Введите число")
D = float(b)**2 - 4*float(a)*float(c)
if D < 0:
    print("Нет решений")
elif D == 0:
    X1 = (-float(b) / 2 * float(a))
    print("есть 1 решение")
    print(X1)
else:
    X1 = (-float(b) + math.sqrt(D)) / (2 * float(a))
    X2 = (-float(b) - math.sqrt(D)) / (2 * float(a))
    print("Возможные решения")
    print(X1)
    print(X2)



