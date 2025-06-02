n = list(map(int, input().zfill(6)))
if sum(n[:3]) == sum(n[3:]):
    print('YES')
else:
    print('NO')
