word_1, word_2 = input().lower(), input().lower()

if word_1[-1] == 'ь':
    if word_1[-2] == word_2[0]:
        print('Good')
    else:
        print('Bad')
else:
    if word_1[-1] == word_2[0]:
        print('Good')
    else:
        print('Bad')
