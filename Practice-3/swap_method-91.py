str1 = input("Enter any string ")
str2 = ""
for ch in str1:
    if 'A' <= ch <= 'Z':
        str2 = str2 + chr(ord(ch) + 32)
    elif 'a' <= ch <= 'z':
        str2 = str2 + chr(ord(ch) - 32)
    else:
        str2 = str2 + ch
#each letter to opposite case if it upper convert ot lower vice-versa
print(str1)
print(str2)