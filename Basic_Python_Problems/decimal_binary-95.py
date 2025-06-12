decimal=int(input("Enter a decimal number: "))
binary=''
while decimal>0:
  binary=str(decimal%2)+binary
  decimal=decimal//2  # Remove the last digit
print("The binary equivalent is:", binary)  # Print the binary equivalent