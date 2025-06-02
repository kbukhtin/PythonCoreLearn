text = input()

if '.' in text and ',' in text:
    print('Нельзя преобразовать')
else:
    if text.replace('.', '', 1).replace(',', '', 1).isdigit():
        print('Можно преобразовать')
    else:
        print('Нельзя преобразовать')
