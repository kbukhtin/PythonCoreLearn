a, b = map(int, input().split())
a_lvl, b_lvl = 3, 2
_count = 0

while b >= a:
    _count += 1
    a *= a_lvl
    b *= b_lvl

print(_count)

