for i in range(1,50,2):
    print(i, end=' ')
print()
#2nd method

n=int(input("Enter a number: "))
i=1
count=0
while count<n:
    print(i, end=' ')
    i += 2
    count += 1