n=int(input("Enter the number: "))
upto=int(input("Enter the number that u want divisible until: "))
for i in range(0, upto + 1):
    if i%n  == 0:
        print(i,end=" ")  # Print if n is divisible by i
    