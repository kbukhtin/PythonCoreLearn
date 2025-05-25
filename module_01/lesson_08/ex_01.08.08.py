n = int(input())
_count = 0;
_count += n // 100
n %= 100
_count += n // 20
n %= 20
_count += n // 10
n %= 10
_count += n // 5
n %= 5
_count += n // 1
n %= 1

print(_count)
