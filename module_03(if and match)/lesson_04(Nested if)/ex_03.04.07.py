s, v1, v2, t1, t2 = map(int, input().split())

playerOne = s * v1 + t1 * 2
playerTwo = s * v2 + t2 * 2

if playerOne == playerTwo:
    print('Friendship')
else:
    if playerOne < playerTwo:
        print('First')
    else:
        print('Second')
