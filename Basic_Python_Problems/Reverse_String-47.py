String=input("Enter a string: ")
rev=""
for i in String:
  rev=i+rev
print("The Reverse of the Given String is:",rev)
print("The Reverse of the Given String is:", String[::-1])  # Using slicing to reverse the string