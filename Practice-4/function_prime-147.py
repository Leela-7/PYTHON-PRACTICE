def isprime(num):
    c=0
    for i in range(1,num+1):
        if num%i==0:
            c=c+1
        if c>2:
            break
    return c==2

number=int(input("Enter any number: "))
if isprime(number):
    print("Prime")
else:
    print("Not Prime")