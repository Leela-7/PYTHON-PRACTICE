x=int(input("Enter the length of side x: "))
y=int(input("Enter the length of side y: "))
z=int(input("Enter the length of side z: "))
if x + y > z and x + z > y and y + z > x:
    if x == y == z:
        print("The triangle is equilateral.")
    elif x == y or y == z or x == z:
        print("The triangle is isosceles.")
    else:
        print("The triangle is scalene.")
else:
    print("The triangle is not possible.")