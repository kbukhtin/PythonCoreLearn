age, member = int(input()), bool(int(input()))

if age > 18 and member:
    print("Цена билета 75")
elif age > 18 and not member:
    print("Цена билета 100")
elif age <= 18 and member:
    print("Цена билета 25")
elif age <= 18 and not member:
    print("Цена билета 50")
