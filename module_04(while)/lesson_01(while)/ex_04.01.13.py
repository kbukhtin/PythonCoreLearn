n, m = map(int, input().split())
_count_m = 0
_c = 0
while n > 0:
    _c += 1
    n -= 1
    _count_m += 1
    if _count_m == m:
        n += 1
        _count_m = 0

print(_c)
