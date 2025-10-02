table = []

maxNumber = 12

for i in range(maxNumber + 1):
    row = []
    for i in range(maxNumber + 1):
        row.append(0)
    table.append(row)

for x in range(maxNumber + 1):
    for y in range(maxNumber + 1):
        row = table[x]
        row[y] = x * y

for i in range(maxNumber + 1):
    print(table[i])
