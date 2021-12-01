x, y = 0, 0
while True:
    a = int(input())
    if a == 0:
        break
    elif a < 0:
        x += a
    elif a > 0:
        y += a
print(f'Сумма отрицательных числе = {y}', f'Сумма положительных числе = {x}', sep='\n')          
