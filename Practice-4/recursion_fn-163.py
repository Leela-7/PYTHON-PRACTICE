def factorial(n):
  global f
  f=1
  for i in range(1,n+1):
    if n==0 or n==1:
      return 1
    else:
      f=f*i
  return f

num=int(input("Enter a number: "))
result=factorial(num)
print(f"The factorial of {num} is {result}")


