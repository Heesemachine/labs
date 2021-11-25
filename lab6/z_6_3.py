import random

a = []
n = int(input("el = "))
for i in range(n):
    a.append(random.randint(0,5))
for el in a:
    if el == 0:
        a.remove(el)
        a.append(el)
print(a)
