if __name__ == '__main__':
    n = int(input())
    student_marks = {}
    for _ in range(n):
        name, *line = input().split()
        scores = list(map(float, line))
        student_marks[name] = scores
    query_name = input()
    a=student_marks[query_name]
    sum=0
    for i in a:
        sum+=i
    avg=sum/len(a)
    print(format(avg,'.2f'))
