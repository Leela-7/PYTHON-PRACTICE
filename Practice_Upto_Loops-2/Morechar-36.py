x = input("Enter the first string: ")
y = input("Enter the second string: ")

if len(x) > len(y):
  print("The longer string is:", x)
elif len(y) > len(x):
  print("The longer string is:", y)
else:
  print("Both strings are of equal length.")