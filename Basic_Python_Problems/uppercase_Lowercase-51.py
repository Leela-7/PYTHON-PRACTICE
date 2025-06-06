ch = input("Enter Single Character: ")

if len(ch) == 1:  # Check if input is exactly one character
    if ch >= 'A' and ch <= 'Z':
        # Convert uppercase to lowercase
        ch = chr(ord(ch) + 32)
        print(ch)
    elif ch >= 'a' and ch <= 'z':
        # Convert lowercase to uppercase
        ch = chr(ord(ch) - 32)
        print(ch)
    else:
        print("Input character is not an alphabet")
else:
    print("Please enter exactly one character")