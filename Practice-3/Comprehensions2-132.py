# Write a program to create 2x2 matrix and display

#Without comprehension
A=[]
for i in range(2):
  row=[]
  for j in range(2):
      value=int(input("Enter Value"))
      row.append(value)
      A.append(row)
      print(A)

# with comprehension
A=[[int(input("Enter Value: ")) for j in range(2)] for i in range(2)]
print(A)