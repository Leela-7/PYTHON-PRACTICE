print("*** MENU ***")
print("1. Area of circle")
print("2. Area of triangle")
print("3. Area of rectangle")
print("4. Exit")

while True:  # Keep showing menu until user exits
    opt = input("Enter your option: ")
    
    if not opt.isdigit():  # Validate numeric input
        print("Please enter a number (1-4)")
        continue
    
    opt = int(opt)
    
    match opt:
        case 1:
            r = float(input("Enter Radius: "))
            area = 3.14159 * r ** 2  # More precise pi value
            print("Area of circle:", round(area, 2))
        case 2:
            b = float(input("Enter Base: "))
            h = float(input("Enter Height: "))
            area = 0.5 * b * h
            print("Area of triangle:", round(area, 2))
        case 3:
            l = float(input("Enter Length: "))
            b = float(input("Enter Breadth: "))
            area = l * b
            print("Area of rectangle:", round(area, 2))
        case 4:
            print("Thanks for using the program!")
            break  # Exit the loop
        case _:
            print("Invalid Option - please try again (1-4)")