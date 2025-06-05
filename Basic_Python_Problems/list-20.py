testlist=[50,100,"lawrence","hello",50,100,True]
a,b,c,d,e,f,g=testlist
testlist.insert(2,"karthik")
testlist.append("hitech")
testlist.remove(100)
testlist[0]="mohan"
print(testlist)
val=testlist.pop(3)
del testlist[1]
print(testlist[2])
print(a)
print(len(testlist))
print(testlist[-2])
print(testlist[1:3])
print(testlist[:3])
print(testlist.index(100))

#Strings
testlist2=["rajesh","mahesh","karthik"]
testlist2.sort()
print(testlist2)
