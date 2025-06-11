x=int(input("Enter first number: "))
y=int(input("Enter second number: "))
operation=input("Select operation (+ - * /):")

if operation == "+":
    print(f"Additon of{x} and {y} is {x+y}")
elif operation == "-":
    print(f"Subtraction of {x} and {y} is{x-y}")
elif operation == "*":
    print(f"Multiplication of {x} and {y} is {x*y}")
elif operation == "/":
    if y == 0:
        print("Error: Division by zero is not allowed.")
    else: 
        print(f"Division of {x} and {y} is {x/y}")
else:
    print("Invalid operation")