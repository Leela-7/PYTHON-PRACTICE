str1=input("Enter a string: ")
index=int(input("Enter the index to delete: "))
x=list(str1)  # Convert string to list for mutability
del x[index]  # Delete the character at the specified index
#x=''.join(x)  # Convert list back to string
print("Original string:", str1)
print("String after deletion:",x)