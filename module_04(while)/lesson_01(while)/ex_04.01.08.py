numbers = [7, 4, 7, 4, 7, 4, 7, 4]
mem = True

while mem:
    if 4 in numbers:
        numbers.remove(4)
    elif 7 in numbers:
        numbers.remove(7)
    else:
        mem = False

print(numbers)
