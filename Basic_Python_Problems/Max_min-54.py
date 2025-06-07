A = [40, 20, 10, 70, 30, 60, 50]
max_value = A[0]
min_value = A[0]

for i in range(len(A)):
    if A[i] > max_value:
        max_value = A[i]
    elif A[i] < min_value:
        min_value = A[i]

print(f'List is {A}')
print(f'Maximum Value: {max_value}')
print(f'Minimum Value: {min_value}')