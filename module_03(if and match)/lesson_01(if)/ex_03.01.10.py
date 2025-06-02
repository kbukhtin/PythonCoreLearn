alfa = 'abcdefgh'
num1, num2 = input(), input()
_isTrueNum1 = (alfa.index(num1[0]) + int(num1[1])) % 2 == 0
_isTrueNum2 = (alfa.index(num2[0]) + int(num2[1])) % 2 == 0
if _isTrueNum1 == _isTrueNum2:
    print('YES')
else:
    print('NO')
