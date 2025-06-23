A=[30,12,34,56,78,56,43,54,55,89,98,79,77,57,41]

#Without comprehension
even=[]
odd=[]
for num in A:
    if num%2==0:
        even.append(num)
    else:
        odd.append(num)
print(even)
print(odd)

#With comprehension
even=[num for num in A if num%2==0]
odd=[num for num in A if num%2!=0]
print(even)
print(odd)