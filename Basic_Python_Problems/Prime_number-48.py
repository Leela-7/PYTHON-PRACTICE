x = int(input("Enter a number: "))
c = 0
if x <= 1:
    print("It is not a prime number")
else:  
    for i in range(1, x + 1):
        if x % i == 0:
            c += 1
            if c > 2:  # Early exit if more than 2 divisors
                print("It is not a prime number")
                break
    else:  # This else corresponds to the for loop (runs if no break occurred)
        if c == 2:
            print("It is a prime number")
        else:
            print("It is not a prime number")