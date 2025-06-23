def read():
  global base,height
  base=float(input("Enter the base of the triangle: "))
  height=float(input("Enter the height of the triangle: "))


def area():
  area=0.5*base*height
  print(f'Area of the Triangle is {area:.2f}')

read()
area()