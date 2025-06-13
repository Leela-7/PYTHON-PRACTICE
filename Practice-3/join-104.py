x="python,java,oracle"
str1=x.split(",")
y=[]
for i in str1:
  y.append(i[::-1])
str2 = " ".join(y)
print(str1)
print(y)