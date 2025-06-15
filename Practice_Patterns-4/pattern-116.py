n=5
for i in range(n):
  for j in range(i):
    print(" ",end="") 
  for k in range(n-i):
    print("* ",end="")
  print()  # Print asterisks in an inverted triangle pattern with spaces