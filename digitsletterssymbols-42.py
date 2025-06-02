string=input("Enter a string: ")
if string.isalnum():
    if string.isalpha():
        print("The string contains only letters.")
    elif string.isdigit():
        print("The string contains only digits.")
    else:
        print("The string contains both letters and digits.")
else:
    print("The string contains special characters.")