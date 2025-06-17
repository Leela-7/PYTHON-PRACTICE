X = {1, 2, 3, 4, 5}
Y = {2, 3, 4, 5, 6}

# Union
A = X.copy()
B = Y.copy()
A.update(B)
print("Union:", A)# represented in |=

# Intersection
A = X.copy()
B = Y.copy()
A.intersection_update(B)
print("Intersection:", A)# represented in &=

# Difference (X - Y)
A = X.copy()
B = Y.copy()
A.difference_update(B)
print("Difference (X - Y):", A)# represented in -=

# Symmetric Difference
A = X.copy()
B = Y.copy()
A.symmetric_difference_update(B)
print("Symmetric Difference:", A)# represented in ^=
