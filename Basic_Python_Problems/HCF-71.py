num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))

a = num1
b = num2

while b != 0:
    temp = b
    b = a % b
    a = temp

print("The HCF of", num1, "and", num2, "is", a)
