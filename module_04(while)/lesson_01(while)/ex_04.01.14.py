a, b = map(int, input().split())
_count = 0

while a > 0:
    _count += 1
    a -= 1
    if _count % b == 0:
        a += 1

print(_count)
