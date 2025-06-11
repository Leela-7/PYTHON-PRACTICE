A=[]
n=int(input("How many integer?"))
for i in range(n):
    value=int(input("Enter any value"))
    A.append(value)

print(f'Before Sorting {A}')

# Bubble Sorting
for i in range(n):
    for j in range(0, n-1):
        if A[j] > A[j+1]:
            A[j], A[j+1] = A[j+1], A[j]

print(f'After Sorting {A}')