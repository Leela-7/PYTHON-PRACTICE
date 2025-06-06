num = int(input("Enter any number: "))
c1 = 0  # Count of unset bits (0s)
c2 = 0  # Count of set bits (1s)

while num > 0:
    r = num % 2    # Get the least significant bit
    if r == 0:
        c1 += 1    # Increment unset bit counter
    else:
        c2 += 1    # Increment set bit counter
    num = num // 2  # Right shift (equivalent to num >> 1)

print(f'Set bit count: {c2}')
print(f'Unset bit count: {c1}')