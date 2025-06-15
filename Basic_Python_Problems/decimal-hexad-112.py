decimal=int(input("Enter a decimal number: "))
function=hex(decimal).replace("0x", "")
print("Hexadecimal representation:", function)
hexadecimal=""
hex="0123456789abcdef"
while decimal>0:
    remainder = decimal % 16
    decimal //= 16
    hexadecimal = hex[remainder] + hexadecimal
print("Hexadecimal representation:", hexadecimal)