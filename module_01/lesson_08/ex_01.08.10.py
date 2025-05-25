sec = int(input())
h = sec // 3600
sec %= 3600
m = sec // 60
sec %= 60

print(h, ':', m // 10, m % 10, ':', sec // 10, sec % 10, sep='')
