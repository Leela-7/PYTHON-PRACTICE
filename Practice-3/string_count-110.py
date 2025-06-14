# str1="abcaaabcd"
# output:4a2b2c1d

str1 = "abcaaabcd"
a_c=0
b_c=0
c_c=0
d_c=0
data=list(str1)
for i in range(0,len(data)):
  if data[i]=="a":
    a_c+=1
  elif data[i]=="b":
    b_c+=1
  elif data[i]=="c":
    c_c+=1
  elif data[i]=="d":
    d_c+=1
print(str(a_c)+"a"+str(b_c)+"b"+str(c_c)+"c"+str(d_c)+"d")


#Second method
# str1 = "abcaaabcd"
# str2 = ""

# for ch in str1:
#     if ch not in str2:
#         str2 = str2 + ch

# print(str1)
# print(str2)

# str3 = ""
# for ch in str2:
#     c = str1.count(ch)
#     str3 = str3 + str(c) + ch

# print(str3)