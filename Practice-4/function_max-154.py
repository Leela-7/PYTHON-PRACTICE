def max(*values):
  if len(values) == 0:
    return None
  m=values[0]
  for value in values:
    if value > m:
      m = value
  return m
total=max(1,2,3,4,5)
print("The maximum is", total)
total=max()
print("The maximum is", total)
A=[1,7,8,9,4,2,3]
print("The maximum is", max(*A))
str="hello Everyone"
print("The maximum is", max(*str))