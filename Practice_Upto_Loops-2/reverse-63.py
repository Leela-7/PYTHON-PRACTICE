num=int(input("Enter a Number:"))
original_num=num
rev=0
while num>0:
    d=num%10
    rev=rev*10+d
    num=num//10
print(f"The Reverse of {original_num} is {rev}")