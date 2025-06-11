start=int(input("Enter the starting number of the interval: "))
end=int(input("Enter the ending number of the interval: "))
for i in range(start, end + 1):
    for j in range(2,i//2 + 1):
        if i % j == 0:
            break
    else:
        print(i,end=" ")