class Student:  # Syntax of defining class
    pass

stud1 = Student()  # Creating object
stud1.rollno = 1
stud1.name = "ramesh"
stud1.course = "python"
print(stud1.rollno, stud1.name, stud1.course)

stud2 = Student()
stud2.rollno = 2
stud2.name = "suresh"
stud2.course = "C++"
print(stud2.rollno, stud2.name, stud2.course)

stud2.course = "Oracle"
print(stud2.rollno, stud2.name, stud2.course)
