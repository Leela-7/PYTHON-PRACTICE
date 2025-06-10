A = []
for i in range(3):
    row = []
    for j in range(3):
        value = int(input("Enter value "))
        row.append(value)
    A.append(row)

B = []
for i in range(3):
    row = []
    for j in range(3):
        row.append(A[j][i])
    B.append(row)

print(A)
print(B)