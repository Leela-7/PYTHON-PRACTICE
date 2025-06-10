n=int(input("Enter the Degrees:"))
x=input("Enter the type of degrees u Entered(C/F):").upper()
if x=="C":
    f=(n*9/5)+32
    print(f"The Fahrenheit of {n} is {f}")
else:
    c=(n-32)*5/9
    print(f"The Celsius of {n} is {c}")