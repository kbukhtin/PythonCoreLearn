a = int(input())
b = int(input())
c = int(input())

value_1 = a + b + c
value_2 = a * b + c
value_3 = a + b * c
value_4 = a * b * c
value_5 = (a + b) * c
value_6 = a * (b + c)

print(max(value_1, value_2, value_3, value_4, value_5, value_6))

