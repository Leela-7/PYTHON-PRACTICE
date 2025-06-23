stud_grades={'naresh':'A',
'suresh':'B',
'ramesh':'A',
'rajesh':'B',
'kishore':'C'}
for name,grade in stud_grades.items():
 print(f'{name}-->{grade}')
stud_gradesA={key:value for key,value in stud_grades.items() if value=='A'}
print(stud_gradesA)
stud_gradesB={key:value for key,value in stud_grades.items() if value=='B'}
stud_gradesC={key:value for key,value in stud_grades.items() if value=='C'}
print(stud_gradesB)
print(stud_gradesC)