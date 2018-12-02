#Квадратное уравнение
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
X1 = (-float(b) + (D ** 2)) / (2*float(a))
X2 = (-float(b) - (D ** 2)) / (2*float(a))
res1 = f"{a} * ({X1} ** 2) + {b} * {X1} + {c}"
res2 = f"{a} * ({X2} ** 2) + {b} * {X2} + {c}"
print(res1)
print(res2)