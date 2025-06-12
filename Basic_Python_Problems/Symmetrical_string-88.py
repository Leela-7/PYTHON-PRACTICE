string=input("Enter a string: ")
if len(string)%2==0:
  x=len(string)//2
  if string[:x]==string[-x:]:
    print("The string is symmetrical")
  else:
    print("The string is not symmetrical")
else:
  print("The string is not symmetrical")