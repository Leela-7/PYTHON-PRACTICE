x=(3,5,2,9,1,4)
k=2
sorted_x=sorted(x)
print(f"The real tuple is: {x}")
print(f"The sorted tuple is: {sorted_x}")

max_min=sorted_x[:k] + sorted_x[-k:]
print(f"The first {k} and last {k} elements of the sorted tuple are: {max_min}")
