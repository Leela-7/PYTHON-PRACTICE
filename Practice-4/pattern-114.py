n = 5
for i in range(n):
    for j in range(i):
        print("  ", end= "")
    for k in range(n-i):
        print('* ',end="")
    print()
# This code prints a left-aligned inverted right angle triangle pattern of asterisks.