num = int(input("Enter any number (100-999): "))
num1 = num
s = 0

while num > 0:
    d = num % 10       # Extract last digit
    s = s + (d ** 3)   # Add cube of digit to sum
    num = num // 10    # Remove last digit

if num1 == s:
    print("Armstrong number")
else:
    print("Not Armstrong number")