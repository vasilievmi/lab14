a1 = int(input())
b1 = int(input())
a2 = int(input())
b2 = int(input())
a3 = max(a1, a2)
b3 = max(b1, b2)
if a3 < b3:
    print(a3, b3)
elif a3 == b3:
    print(a3)
else:
    print('Пустое множество')
