x_count, y_count, z_count = map(int, input().split())
x_price = 3
y_price = x_price + 2
z_price = y_price + 7
total = x_count * x_price + y_count * y_price + z_count * z_price
print(total)