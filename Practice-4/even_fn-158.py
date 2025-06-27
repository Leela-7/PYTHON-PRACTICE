def even(m,n):
  for num in range(m,n):
    if num%2==0:
      yield num

x=even(1,21)
for value in x:
  print(value, end=" ")