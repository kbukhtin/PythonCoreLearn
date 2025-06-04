a, b, c = map(int, input().split())
_min, _max = 0, 0
if a < b:
    if a < c:
        _min = a
    else:
        _min = c
else:
    if b < c:
        _min = b
    else:
        _min = c

if a > b:
    if a > c:
        _max = a
    else:
        _max = c
else:
    if b > c:
        _max = b
    else:
        _max = c

print(_max - _min)
