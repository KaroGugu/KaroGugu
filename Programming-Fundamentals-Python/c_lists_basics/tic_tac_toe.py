row_1 = input().split(' ')
row_2 = input().split(' ')
row_3 = input().split(' ')

# list for each of the rows
r1 = []
r2 = []
r3 = []


for a in row_1:
    r1.append(int(a))
for b in row_2:
    r2.append(int(b))
for c in row_3:
    r3.append(int(c))

# list for each of the three columns

c1 = [r1[0], r2[0], r3[0]]
c2 = [r1[1], r2[1], r3[1]]
c3 = [r1[2], r2[2], r3[2]]

# list for each of the two diagonals
x1 = [r1[0], r2[1], r3[2]]
x2 = [r1[2], r2[1], r3[0]]

if r1.count(2) == 3 or r2.count(2) == 3 or r3.count(2) == 3 \
        or c1.count(2) == 3 or c1.count(2) == 3 or c1.count(2) == 3 \
        or x1.count(2) == 3 or x2.count(2) == 3:
    print("Second player won")

elif r1.count(1) == 3 or r2.count(1) == 3 or r3.count(1) == 3 \
        or c1.count(1) == 3 or c1.count(1) == 3 or c1.count(1) == 3 \
        or x1.count(1) == 3 or x2.count(1) == 3:
    print('First player won')
else:
    print('Draw!')
