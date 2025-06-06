a=int(input("Enter First Number :"))
b=int(input("Enter Second Number :"))
print("Before swaping ",a,b)
c=a#3rd variable
a=b
b=c
print("After swaping ",a,b)
#without using 3rd variable
a=a+b
b=a-b
a=a-b
print("After swaping ",a,b)
a,b=b,a
print("After swaping ",a,b)