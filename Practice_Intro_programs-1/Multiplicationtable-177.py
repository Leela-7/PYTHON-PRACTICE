def print_table(number):
    print(f"\nMultiplication Table for {number}:")
    for i in range(1, 11):
        print(f"{number} x {i} = {number * i}")

# Calling the function
num = int(input("Enter a number: "))
print_table(num)
