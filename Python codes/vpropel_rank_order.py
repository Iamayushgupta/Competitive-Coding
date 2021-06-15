students_group={}
n=int(input())
for i in range(0,n):
    details=input().split()
    score=int(details[1])*10 + int(details[2])*30 + int(details[3])*50
    if not students_group.get(score):
        students_group[score]=[details[0]]
    else:
        students_group[score].append(details[0])

scores=list(students_group.keys())
scores.sort(reverse=True)

rank=1
for score in scores:
    students=students_group[score]
    students.sort()
    for student in students:
        print(rank,student)
        rank+=1