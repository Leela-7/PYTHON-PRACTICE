dict1={n:n**2 for n in range(1,11)}
print(dict1)
dict2={n:chr(n) for n in range(65,91)}
print(dict2)
dict3={chr(n):n for n in range(97,123)}
print(dict3)
dict3={num:[num*i for i in range(1,11)] for num in range(1,6)}
print(dict3)
for key,value in dict3.items():
 print(key,value)