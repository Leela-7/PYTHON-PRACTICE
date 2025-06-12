str1 = input("Enter any string ")
str2 = ""
for i in range(len(str1)):
    if i == 0:
        if 'A' <= str1[i] <= 'Z':
            str2 = str2 + str1[i]
        elif 'a' <= str1[i] <= 'z':
            str2 = str2 + chr(ord(str1[i]) - 32)
        else:
            str2 = str2 + str1[i]
    elif 'A' <= str1[i] <= 'Z':
        str2 = str2 + chr(ord(str1[i]) + 32)
    else:
        str2 = str2 + str1[i]
#first letter of word to uppercase
print(str1)
print(str2)