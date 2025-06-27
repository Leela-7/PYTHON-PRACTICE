def str():#Outer function
  x=100
  def str2():#Inner function
    y=200
    print(x)
    print(y)
  def str3():
    x=300
    print(x)
  str2()
  str3()
str()