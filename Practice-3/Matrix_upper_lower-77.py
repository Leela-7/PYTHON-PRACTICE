A = []
print("Input elements of matrix")
for i in range(3):
    row = []
    for j in range(3):
        value = int(input("Enter value "))
        row.append(value)
    A.append(row)
print("\nMatrix A:")
for row in A:
    print(row)
print()
print("Upper Triangle")
for i in range(3):
    for j in range(3):
        if j >= i:
            print(A[i][j], end=' ')
        else:
            print(" ", end=" ") 
    print()

print()
print("Lower Triangle")
for i in range(3):
    for j in range(3):
        if i >= j:
            print(A[i][j], end=' ')
        else:
            print(" ", end=" ") 
    print()