A_matrix = []
B_matrix = []
C_matrix = []

print("\nInput Elements of first matrix (2x2)")
for i in range(2):
    row = []
    for j in range(2):
        value = int(input(f"Enter value for A[{i}][{j}]: "))
        row.append(value)
    A_matrix.append(row)

print("Input Elements of second matrix (2x2)")
for i in range(2):
    row = []
    for j in range(2):
        value = int(input(f"Enter value for B[{i}][{j}]: "))
        row.append(value)
    B_matrix.append(row)

print("\nMatrix A:")
for row in A_matrix:
    print(row)

print("Matrix B:")
for row in B_matrix:
    print(row)

for i in range(2):
    row = []
    for j in range(2):
        row.append(A_matrix[i][j] + B_matrix[i][j])
    C_matrix.append(row)

print("\nMatrix C (A + B):")
for row in C_matrix:
    print(row)