a=int(input("Enter angle of a triangle:"))
b=int(input("Enter angle of a triangle:"))
c=int(input("Enter angle of a triangle:"))
if a+b+c==180:
    if a == 90 or b == 90 or c == 90:
        print(" right angle triangle")
    else:
        print(" not right angle triangle")
else:
    print("not a triangle")