n=int(input("Enter a Number:"))
sum=0
while n>0:
  d=n%10
  sum+=d
  n=n//10
print(f"The Sum of digits is {sum}")