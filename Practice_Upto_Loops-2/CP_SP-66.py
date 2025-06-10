cp=int(input("Enter the cost price: "))
sp=int(input("Enter the selling price: "))
x=cp-sp
if x>0:
    print("Loss")
    print(f"Loss amount is {x}")
elif x<0:
    print("Profit")
    print(f"Profit amount is {abs(x)}")
else:
    print("No Profit No Loss")