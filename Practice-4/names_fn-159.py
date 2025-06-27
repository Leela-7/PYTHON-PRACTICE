names=["naresh","kumar","suresh","ramesh","mahesh"]
names1=list(map(lambda x: x.upper(), names))
print("Original names:", names)
print("Uppercase names:", names1)
A=[1,2,3,4,5]
B=list(map(lambda num:num**2, A))
print("Original list:", A)
print("Squared list:", B)
C=["10","20","30","40"]
D=list(map(int,C))
print(C,D,sep="\n")
E=[1,2,3,4,5]
F=[10,20,30,40,50]
G=list(map(lambda x,y:x+y,E,F))
print(E,F,G,sep="\n")