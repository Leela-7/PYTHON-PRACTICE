decimal=int(input("Enter a decimal number: "))
octal=''
while decimal>0:
  octal=str(decimal%8)+octal
  decimal=decimal//8  # Remove the last digit
print("The octal equivalent is:", octal)  # Print the binary equivalent