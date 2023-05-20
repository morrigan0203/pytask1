""" for i in range(2, 10):
    for j in range(1, 11):
        print(i, "*", j, "=", i * j)
    print() """


for i in range(1, 11):
    for j in range(2, 6):
        print(f'{j} * {i:>2} = {i * j:>2}', end=' '*3)
    print()
print()

for i in range(1, 11):
    for j in range(6, 10):
        print(f'{j} * {i:>2} = {i * j:>2}', end=' '*3)
    print()