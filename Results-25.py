marks=int(input("Enter a Number:"))
if marks >=35:
    print("You passed exam")
    if marks >=90:
          print("Your grade is A")
    elif marks <90 and marks >=80:
        print(" your grade is B")
    elif marks <80 and marks>=70:
        print("Your grade is C+")
    elif marks <70 and marks>=60:
        print("Your grade is C")
    elif marks <60 and marks>=50:
        print("Your grade is D+")
    elif marks <50 and marks>=36:
        print("Your grade is D+")
else:
    print("You failed the Exam",marks)