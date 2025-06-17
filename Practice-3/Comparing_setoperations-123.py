A={1,2,3,4,5}
B={1,2,3}
print(A.issubset(B))  # <= check whether element  in the set is in other
print(A.issuperset(B))  # >=Test whether every element in other is in the set.
print(A.isdisjoint(B))  # Check if A and B have no elements in common