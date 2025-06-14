# str1="4a2b2c1d"
# output:aaaabbccd

str1 = "4a2b2c1d"
output = ""
i=0
while i < len(str1):
    count = int(str1[i])  # Get the count of characters
    char = str1[i + 1]    # Get the character
    output += char * count  # Append the character 'count' times
    i += 2  # Move to the next character and its count
print(output)  # Output: aaaabbccd



#4*a+2*b+2*c+1*d
#second method

# str1 = "4a2b2c1d"
# str2 = ""

# for i in range(0, len(str1), 2):
#     n = int(str1[i])
#     ch = str1[i+1]
#     str2 = str2 + (n * ch)

# print(str1)
# print(str2)