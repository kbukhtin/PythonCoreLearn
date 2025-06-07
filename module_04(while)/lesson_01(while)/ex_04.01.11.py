n = int(input())
mem = 1

while (x := mem ** 2) <= n:
    print(x)
    mem += 1
