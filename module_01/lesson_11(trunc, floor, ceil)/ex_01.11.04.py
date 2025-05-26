from math import ceil

jar_paint = 16

l, w, h = map(int, input().split())
s = 2 * h * (l + w)

print(ceil(s / jar_paint))
