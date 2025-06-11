string=input("Enter a string: ")
rev=""
for i in string:
  rev=i+rev

if string==rev:
  print("The string is a palindrome")
else:
  print("The string is not a palindrome")