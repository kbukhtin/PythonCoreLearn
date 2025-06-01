numbers = [-214, 181, -139, 448, -20, -917, 32, 422, -895, 198, 284, 472, -986, -964, -989, 29]
result = []

result.append(numbers.pop())
result.append(numbers.pop(0))
result.append(numbers.pop(12))
result.append(numbers.pop(7))

print(numbers)
print(sum(result))
