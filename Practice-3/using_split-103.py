x,y=map(int,input("Enter x and y separated by space: ").split())
print(x, type(x))
print(y, type(y))

t=int(input("Enter number of test cases: "))
for i in range(t):
  num1,num2=map(int,input("Enter two numbers separated by space: ").split())
  if (num1+num2)%2==0:
      print("Even")
  else:
      print("Odd")
     