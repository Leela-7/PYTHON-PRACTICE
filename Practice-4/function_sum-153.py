def sum(*values):
  s=0
  for value in values:
    s+=value
  return s
total=sum(1,2,3,4,5)
print("The sum is", total)
total=sum()
print("The sum is", total)
total=sum(1.5,2.5,6.5)
print("The sum is", total)