#Фибоначчи
first = 1
second = 2

i = 2
n = input("какой элемент (указывать целое число!) из ряда вам нужен?: ")
while n.isdigit() is False or int(n) < 0:
    n = input("какой элемент (указывать целое число!) из ряда вам нужен?: ")
while i < int(n):
    the_sum = first + second
    first = second
    second = the_sum
    i += 1
print(the_sum)

