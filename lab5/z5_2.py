import random

n = int(input("кіслькість чисел = "))
a = [random.randint(0,100) for el in range(n)]
print(a)
for el in a:
    print("елемент : {0} порядковий номер {1}".format(el,a.index(el)))