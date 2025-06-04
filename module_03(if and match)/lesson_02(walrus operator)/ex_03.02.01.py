if (money := int(input())) > 10_000:
    print(f'Ого! {money}! Куда вам столько? Мы заберем {money - 10_000}')
else:
    print(f'Сумма {money} не превышает лимит, проходите')
