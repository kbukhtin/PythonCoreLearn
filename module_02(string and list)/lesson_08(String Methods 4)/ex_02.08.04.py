red, green, blue = int(input()), int(input()), int(input())
result = '#' + hex(red)[2:].zfill(2) + hex(green)[2:].zfill(2) + hex(blue)[2:].zfill(2)
print(result.upper())
