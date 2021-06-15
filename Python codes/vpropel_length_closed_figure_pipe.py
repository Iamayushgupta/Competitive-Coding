di = {}
for _ in range(int(input())):
    a,b = map(int, input().split())
    di[a] = b

check_point = int(input())

current = check_point
ans = 0
while (current in di):
    ans += 1
    current = di[current]
    if (current == check_point):
        break

if (current != check_point):
    print(0)
else:
    print(ans)