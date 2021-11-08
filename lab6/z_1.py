#Дано n дійсних чисел: x1,x2,...,xn . Знайти найбільше серед від’ємних.
n = int(input("n= "))
a = []
for i in range(n):
    x = float(input('x{0}= '.format(i)))
    a.append(x)
while x < 0:
    max = x
    print(max)
    break
