s=input()
def to_hour(s):
    if 'P.M' in s:
        if int(s[:2]) < 12:
            x=str(int(s[:2]) + 12)
            y=x + s[2:8]
        else:
            y=s[:8]
    elif 'A.M' in s:
        if int(s[:2])==12:
            y='00'+ s[2:8]
        else:
            y=s[:8]
    elif 'midnight' in s:
        y='00:00:00'
    else:
        y=s[:8]
    return y
x=to_hour(s)

def eight_hour(y):
    if y=='00:00:00':
        z='08:00:00 midnight'
    elif int(y[:2])>=0 and int(y[:2])<=7:
        z=y + ' A.M'
    elif y=='08:00:00':
        z='08:00:00 midmorning'
    elif int(y[:2])>=8 and int(y[:2])<=15:
        a=str(int(y[:2])-8)
        z='0'+str(a)+y[2:8] + ' B.M'
    elif y=='16:00:00':
        z='08:00:00 midevening'
    else:
        a=str(int(y[:2])-16)
        z='0'+str(a)+y[2:8]+' C.M'
    return z
print(eight_hour(x))