#question 2 (a) ieee
alp_list = ['A', 'B', 'C', 'D', 'E', 'F']
rev_list = ['E', 'D', 'C', 'B', 'A']
x = 6
y = 5
for i in range(1, 6):
    for j in range(x):
        print(alp_list[j], end='')
    x -= 1
    print()

y = 1
for i in range(6):
    for j in range(y):
        print(alp_list[j], end='')
    y += 1
    print()

# question 2 (b) ieee (COMPLETE)

for i in range(1, 8):
    for j in range(1, 8):
        if i == 1 or i == 7 or i + j == 8:
            print('*', end='')
        else:
            print(' ', end='')
    print()
