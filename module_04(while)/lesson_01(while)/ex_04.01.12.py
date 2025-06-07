x, y = map(int, input().split())
_c = 1
while x < y:
    _c += 1
    x += x * 15 / 100

print(_c)
