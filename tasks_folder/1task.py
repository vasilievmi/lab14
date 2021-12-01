n = int(input("Введите кол-во членов ряда: "))
s = 0
x = int(input("Введите икс: "))
for i in range(1, n+1):
    s += (3*i+2)*(x ** (i-2))
print (s)
