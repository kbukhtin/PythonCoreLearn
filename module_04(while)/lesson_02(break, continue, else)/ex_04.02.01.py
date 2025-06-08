word = input()

while len(word) != 0:
    if word[0] == 'e' or word[0] == 'a':
        print('Ага! Нашлась')
        break
    print(f'Текущая буква: {word[0]}')
    word = word[1:]
else:
    print('Распечатали все буквы')
