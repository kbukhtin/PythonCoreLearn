money = list(map(int, input().split()))
finish, avg_result = int(input()), 0

while money:
    avg_result += money.pop(0)
    if avg_result >= finish:
        print(avg_result)
        print('Цель достигнута')
        break
else:
    print(avg_result)
    print('Цель не достигнута')
