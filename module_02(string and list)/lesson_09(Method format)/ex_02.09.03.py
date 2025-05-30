number = int(input())
text1 = 'Для числа {n1} предыдущим будет число {n2}.'.format(n1 = number, n2 = number - 1)
text2 = 'Для числа {n1} следующим будет число {n2}.'.format(n1 = number, n2 = number + 1)
print(text1, text2, sep='\n')
