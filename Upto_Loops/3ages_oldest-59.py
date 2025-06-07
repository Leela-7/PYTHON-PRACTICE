#first Method
n1=int(input(f"Enter the ageof person 1"))
n2=int(input(f"Enter the ageof person 2"))
n3=int(input(f"Enter the ageof person 3"))
if n1>n2 and n1>n3:
    print(f"Person 1 is the oldest with age {n1}")
elif n2>n1 and n2>n3:
    print(f"Person 2 is the oldest with age {n2}")
else:
    print(f"Person 3 is the oldest with age {n3}")

#second Method
ages=[]
for i in range(3):
    age=int(input(f"Enter the age of person {i+1}: "))
    ages.append(age)
max_age= max(ages)
oldest_person = ages.index(max_age) + 1
print(f"Person {oldest_person} is the oldest with age {max_age}")

#third Method
ages=[]
for i in range(3):
    age=int(input(f"Enter the age of person {i+1}: "))
    ages.append(age)
max=ages[0]
for i in range(len(ages)):
    if ages[i]>max:
        max=ages[i]
        oldest_guy=i+1
print(f"Person {oldest_guy} is the oldest with age {max}")
