num = int(input("Enter a number: "))
n = abs(num)  # Handle negative numbers
c = 0

if n == 0:
    c = 1  # Zero is a single-digit number
else:
    while n > 0:
        n //= 10
        c += 1

if c == 1:
    print("It is a single digit value")
elif c == 2:
    print("It is a two digit value")
elif c == 3:
    print("It is a three digit value")
else:
    print("It is greater than three digit values")