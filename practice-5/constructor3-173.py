class Marks:
    def __init__(self, r, n, s1, s2, s3):
        self.rollno = r
        self.name = n
        self.sub1 = s1
        self.sub2 = s2
        self.sub3 = s3

stud1 = Marks(1, "naresh", 60, 50, 80)
stud2 = Marks(2, "suresh", 70, 80, 90)

print(stud1.rollno, stud1.name, stud1.sub1, stud1.sub2, stud1.sub3)
total = stud1.sub1 + stud1.sub2 + stud1.sub3
avg = total / 3
print(total, avg)

print(stud2.rollno, stud2.name, stud2.sub1, stud2.sub2, stud2.sub3)
