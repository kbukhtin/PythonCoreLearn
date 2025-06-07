n = int(input())
n_1 = int(str(n)[0])
mem = True

while mem:
    n *= n_1
    n_1 = int(str(n)[0])

    if n_1 == 1:
        mem = False
    elif n >= 1_000_000_000:
        mem = False

print(n)
