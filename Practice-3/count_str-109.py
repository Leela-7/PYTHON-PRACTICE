str_variable = "java python c c++ java python data .net telugu crm"
count_java = 0
count_python = 0

words = str_variable.split()
print("Words in the string:", words)

for word in words:
    if word == "java":
        count_java += 1
    elif word == "python":
        count_python += 1

print(f"Number of 'java' occurrences: {count_java}")
print(f"Number of 'python' occurrences: {count_python}")


#second  method
# str1="java python java oracle java .net java mysql"
# str2="java"
# i=0
# c=0
# while True:
#     index=str1.find(str2,i)
#     if index!=-1:
#         c+=1
#     else:
#        break
#     i=index+1
# print(str1)
# print(c)