def power(n):
  def inner(p):
    w=n**p
    print(f"{n} raised to the power of {p} is {w}")
  return inner

x=power(25)
x(2)

x=power(10)
x(2)




