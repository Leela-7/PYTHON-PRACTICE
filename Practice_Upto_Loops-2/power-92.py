n=int(input("Enter the number: "))
power=int(input("Enter the number that u want power until: "))

for i in range(1, power + 1):
    print(f"{n} ^ {i} = {n ** i}")  # Using exponentiation operator to calculate power