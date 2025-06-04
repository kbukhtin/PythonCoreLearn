n = int(input())

if n >= 65:
    print('Пожилой человек')
elif 19 <= n < 65:
    print('Взрослый человек')
elif 12 <= n < 19:
    print('Подросток')
elif 4 <= n < 12:
    print('Ребенок')
elif 2 <= n < 4:
    print('Малыш')
elif n < 2:
    print('Младенец')
