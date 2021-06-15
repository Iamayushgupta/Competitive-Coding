from itertools import groupby
s1='abcde'
s2='ecfgd'

x=''.join(k for k, g in groupby((s1)))
y=''.join(k for k, g in groupby((s2)))


a=list(set(s1)&set(s2))
empty_list=[]
for i in a:
    p=x.index(i)
    q=y.index(i)
    empty_list.append(x[:p] + y[q:])
    empty_list.append(y[:q] + x[p:])

final=sorted(empty_list)
for item in final:
    print(item)