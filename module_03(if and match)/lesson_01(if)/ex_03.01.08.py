a, b, c = int(input()), int(input()), int(input())
if a < b + c and b < a + c and c < a + b:
    if a == b or b == c or a == c:
        print('YES')
    else:
        print('NO')
else:
    print('NO')
