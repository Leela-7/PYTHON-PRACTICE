a = int(input("Enter coefficient a: "))
b = int(input("Enter coefficient b: "))
c = int(input("Enter coefficient c: "))

if a == 0:
  print("Invalid Quadrilateral equation.")
else:
  print(f"Quadratic equation is:{a}x^2 +{b}x +{c}")
  discriminant = b * b - 4 * a * c
  square_dis = discriminant **0.5
  denominator = 2*a
  if discriminant > 0:
    # If b*b > 4*a*c, then roots are real and different; roots of x2 - 7x - 12 are 3 and 4
    print("Real and different roots")
    print("Roots: ", -b-square_dis/denominator, " and ", -b+square_dis/denominator )


  elif discriminant == 0:
    # b*b == 4*a*c, then roots are real and both roots are same; roots of x2 - 2x + 1 are 1 and 1
    print("Real and same roots")
    print("Roots are: ", -b/denominator)

  else:
    # If b*b < 4*a*c, then roots are complex; x2 + x + 1 roots are -0.5 + i1.73205 and -0.5 - i1.73205
    print("Complex roots")
    print("Roots are: ", -b/denominator,"+i and ", -b/denominator,"-i")