def average(student_marks,query_name):
    sum = 0
    num = 0
    for i in student_marks[query_name]:
        sum += i
        num += 1

    result = sum/num


    print("%.2f" % result)

n = int(input())
student_marks = {}
for _ in range(n):
    name, *line = input().split()
    scores = list(map(float, line))
    student_marks[name] = scores
query_name = input()

average(student_marks,query_name)

