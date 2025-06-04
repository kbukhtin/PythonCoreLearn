text = input()

if text[-1] == '.':
    print('Законченное')
elif text[-1] == ',':
    print('Незаконченное')
elif text[-1] == '?':
    print('Вопросительное')
elif text[-1] == '!':
    print('Восклицательное')
else:
    print('Неопределенное')
