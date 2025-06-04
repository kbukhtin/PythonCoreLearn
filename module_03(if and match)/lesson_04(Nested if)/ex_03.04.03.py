text = input()
result = ['четная', 'нечетная', 'короткая', 'большая']
_count = len(text)
if _count % 2 == 0:
    if _count < 6:
        print(result[0], result[2])
    else:
        print(result[0], result[3])
else:
    if _count < 6:
        print(result[1], result[2])
    else:
        print(result[1], result[3])
