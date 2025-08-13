if __name__ == '__main__':
    students = []
    for _ in range(int(input())):
        name = input()
        score = float(input())
        students.append([name, score])
    
    # Get all grades
    grades = sorted(set([s[1] for s in students]))
    second_lowest = grades[1]
    
    # Filter students with the second lowest grade
    result = [s[0] for s in students if s[1] == second_lowest]
    for name in sorted(result):
        print(name)