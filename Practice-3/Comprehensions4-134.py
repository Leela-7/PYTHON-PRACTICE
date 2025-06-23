grades=[["naresh","A"],
["suresh","B"],
["ramesh","C"],
["kishore","B"],
["rajesh","A"]]


# Without comprehension
Grade_A=[]
Grade_B=[]  
Grade_C=[]
for student in grades:
    if student[1]=="A":
        Grade_A.append(student)
    elif student[1]=="B":
        Grade_B.append(student)
    elif student[1]=="C":
        Grade_C.append(student)
print("Grade A Students:", Grade_A)
print("Grade B Students:", Grade_B)
print("Grade C Students:", Grade_C)


# With comprehension
Grade_A=[student for student in grades if student[1]=="A"]
Grade_B=[student for student in grades if student[1]=="B"]
Grade_C=[student for student in grades if student[1]=="C"]
print("Grade A Students:", Grade_A)
print("Grade B Students:", Grade_B) 
print("Grade C Students:", Grade_C)