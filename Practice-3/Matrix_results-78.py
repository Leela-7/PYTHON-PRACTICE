marks = []
print("Input Marks")
for i in range(3):
    row = []
    for j in range(3):
        m = int(input(f'Student{i+1} Subject{j+1} Marks '))
        row.append(m)
    marks.append(row)

for row in marks:
    total = sum(row)
    avg = total / 3
    result = "PASS" if row[0] >= 40 and row[1] >= 40 and row[2] >= 40 else "FAIL"
    print(f'{row}\t{total}\t{avg:.2f}\t{result}')