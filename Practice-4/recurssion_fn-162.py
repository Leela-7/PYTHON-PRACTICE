def fun():
  print("Hello, World!")
  fun()
fun()

# This code will cause a RecursionError due to infinite recursion.
# To avoid this, you can add a base case to stop the recursion after a certain conditions
