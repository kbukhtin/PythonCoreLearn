import math

a, b, c = int(input()), int(input()), int(input())

a = math.ceil(a / 2)
b = math.ceil(b / 2)
c = math.ceil(c / 2)

print(a + b + c)
