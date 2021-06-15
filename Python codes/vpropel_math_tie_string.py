n = int(input())


def num_to_str(num):
    s = ""
    while len(s) != 20:
        if num % 3 == 0:
            s += 'r'
        elif num % 3 == 1:
            s += 'g'
        elif num % 3 == 2:
            s += 'b'
        num = num//3
    return (s[::-1])


def str_to_num(s):
    dic = {"r": 0, "g": 1, "b": 2}
    z = 0
    for i in s:
        z = 3*z + dic[i]
    return z


def str_check_1(a1, a2):
    count = 0
    for i in range(20):
        if a1[i] != a2[i]:
            count += 1
    if count == 1:
        return True


def str_check_2(a1, a2):
    count = 0
    for i in range(20):
        if a1[i] != a2[i]:
            count += 1
    if count == 2:
        return True


num1 = n+1
while True:
    p = num_to_str(n)
    q = num_to_str(num1)
    if str_check_1(p, q):
        temp1 = q
        break
    num1 += 1

num2 = n+1
while True:
    a = num_to_str(n)
    b = num_to_str(num2)
    if str_check_2(a, b):
        temp2 = b
        break
    num2 += 1

print(str_to_num(temp1), end='\t')
print(str_to_num(temp2))
print(num_to_str(n))
print(temp1)
print(temp2)
