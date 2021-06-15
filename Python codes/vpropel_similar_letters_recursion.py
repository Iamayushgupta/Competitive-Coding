w=input()
w.lower()
bool=True
if len(w)==1:
	print('0')
	bool=not bool
def star(word):
	temp=''
	if len(word)>1:
		if word[0]!=word[1]:
			temp+=word[0]
	if len(word)>2:
		for i in range(1,len(word)-1):
			if word[i-1]!=word[i] and word[i]!=word[i+1]:
				temp+=word[i]
	if len(word)>1:
		if word[-1]!=word[-2]:
			temp+=word[-1]
	return (temp)
print(star(w))
while bool:
	x=star(w)
	y=star(x)
	if y!=x:
		w=x
		x=y
	else:
		if len(x)==0:
			print('1')
			break
		else:
			print('0')
			break