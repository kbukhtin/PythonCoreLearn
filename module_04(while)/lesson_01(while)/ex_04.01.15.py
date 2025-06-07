n = int(input())
a, mem = 0, True
while mem:
    x = 2 ** a
    if x < n:
        a += 1
    elif x == n:
        mem = False
    else:
        a = 'НЕТ'
        mem = False
print(a)
