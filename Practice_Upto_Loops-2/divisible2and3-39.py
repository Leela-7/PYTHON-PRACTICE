num=int(input("Enter a number: "))
if num % 2 == 0:
  if num%3==0:
    print("The number is divisible by both 2 and 3.")
  else:
    print("The number is divisble by 2 only.")
else:
  if num % 3 == 0:
    print("The number is divisible by 3 only.")
  else:
    print("The number is not divisible by either 2 or 3.")