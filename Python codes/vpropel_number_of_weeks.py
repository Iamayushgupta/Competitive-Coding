def get_weeks(cost,money,inc):
    if money>=cost:
        return 1

    weeks=0
    current_money=money
    total_money=0
    while total_money<cost:
        total_money+=current_money
        money+=inc
        weeks+=1
    return weeks   


cost=int(input('enter cost: '))
money=int(input('enter money per week: '))
inc=int(input('enter increment: '))

print(get_weeks(cost,money,inc))
