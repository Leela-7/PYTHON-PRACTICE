str1 = input("Enter any string ")
str2 = ""
i = 0
l = len(str1)
while i < l:
    if i == 0:
        if 'A' <= str1[i] <= 'Z':
            str2 = str2 + str1[i]
        elif 'a' <= str1[i] <= 'z':
            str2 = str2 + chr(ord(str1[i]) - 32)
        else:
            str2 = str2 + str1[i]
    elif str1[i] == ' ':
        str2 = str2 + str1[i]
        if i + 1 < l:
            i += 1
            if 'a' <= str1[i] <= 'z':
                str2 = str2 + chr(ord(str1[i]) - 32)
            else:
                str2 = str2 + str1[i]
    elif 'A' <= str1[i] <= 'Z':
        str2 = str2 + chr(ord(str1[i]) + 32)
    else:
        str2 = str2 + str1[i]
    i = i + 1
# first letter of each word to uppercase in the sentence
print(str1)
print(str2)