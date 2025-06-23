x=20
y=30

def add():
  print(f'Addition of {x} and {y} is {x+y}')

def sub():
  print(f'Subtraction of  {x} and {y} is {x-y}')

def mul():
  print(f'Multiplication of {x} and {y} is {x*y}')

def div():
  if y==0:
    print("Division by zero is not allowed")
  else:
    print(f'Division of {x} and {y} is {x/y:.2f}')


add()
sub()
mul()
div()