x=int(input("Enter the number: "))
count=0
while x>0:
    x=x//10  # Remove the last digit
    count+=1  # Increment the count for each digit removed
print("The number of digits is:", count)  