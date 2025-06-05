num=int(input("Enter a Number: "))
rev=0
while num>0:
    digit=num%10
    rev=rev*10+digit
    num=num//10
print("The Reverse of the Given Number is:",rev)
# Using slicing to reverse the number (after converting to string)
n1 = input("Enter a Number: ")
print("The Reverse of the Given Number is:", n1[::-1])