a, b, c = map(int, input().split())

_max = max(a, b, c)
_min = min(a, b, c)
_avg = (a + b + c) - _max - _min

print(pow(_max, 2) == pow(_min, 2) + pow(_avg, 2))
