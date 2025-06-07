n = list(map(int, input().split()))
mem = 1

while mem:
    if 4 in n:
        n.remove(4)
    elif 7 in n:
        n.remove(7)
    elif n.count(5) < 10:
        n.append(5)
    else:
        mem = 0

print(n)
