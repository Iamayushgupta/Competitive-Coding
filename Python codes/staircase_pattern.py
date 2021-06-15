n = int(input())

for i in range(1, n+1):
    print(' '*(n-1) + '#'*i)
    n = n-1

for i in range(n):
    print('#'*(i+1))