def pos(n):
  if n>0:
    return "Positive"
  elif n<0:
    return "Negative"
  else:
    return "Zero"

number=int(input("Enter a number: "))
check=pos(number)
print("The number is", check)
