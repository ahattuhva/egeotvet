from itertools import product
numbers = product('01234567', repeat=5)
k=0
for n in numbers:
    print(n)
