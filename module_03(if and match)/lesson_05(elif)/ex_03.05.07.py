a, b, sign = float(input()), float(input()), input()

if b == 0 and sign == '/' or sign not in '+-*/':
    print('Неизвестно')
elif sign == '+':
    print(a + b)
elif sign == '-':
    print(a - b)
elif sign == '*':
    print(a * b)
elif sign == '/':
    print(a / b)
