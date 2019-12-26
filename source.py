if __name__ == '__main__':
    n = int(input())
    student_marks = {}
    for _ in range(n):
        name, *line = input().split()
        scores = list(map(float, line))
        student_marks[name] = scores
    query_name = input()
    query_name_score = list(student_marks[query_name])
    phy = query_name_score[0]
    math = query_name_score[1]
    chem = query_name_score[2]
    sum = float(phy)+float(math)+float(chem)
    avg = (sum/3)
    print("{0:.2f}".format(avg))
