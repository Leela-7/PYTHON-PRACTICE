n = int(input("Enter number: "))

original_num = n
rev = 0

while n > 0:
    digit = n % 10          
    rev = rev * 10 + digit  
    n = n // 10       
if original_num == rev:
    print("The number is a palindrome!")
else:
    print("The number isn't a palindrome!")
