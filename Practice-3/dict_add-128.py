marks = {}
n = int(input("How many students? "))
for i in range(n):
    name = input("Name: ")
    sub = []
    for j in range(3):
        s = int(input("Marks: "))
        sub.append(s)
    marks[name] = sub

for t in marks.items():
    name, sub = t
    tot = sum(sub)
    avg = tot / 3
    result = "PASS" if sub[0] >= 40 and sub[1] >= 40 and sub[2] >= 40 else "FAIL"
    print(f'{name}\t{sub}\t{tot}\t{avg:.2f}\t{result}')
