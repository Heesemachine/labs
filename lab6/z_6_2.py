n = int(input("Введіть довжину масиву : "))
a = []
s = sum = 1
for i in range(1,n+1) :
    s = s*((-1)**i)*i
    a.append(s/i)
    if a[i-1] > 0 :
        sum = sum + a[i-1]
print("сума = {0}".format(sum))

