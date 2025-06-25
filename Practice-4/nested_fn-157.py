def str1():
  print("This is the outer function")
  def str2():
    print("This is the inner function")
  str2()
str1()

# This code demonstrates the use of nested functions in Python.
# This function illustrates the concept of varaible assigning in the loop

def fun1():
  x=200
  def fun2():
    print(x)
  fun2()

def fun3():
  def fun4():
    x=100
    return x
  x=fun4()
  print(x)

fun1()
fun3()