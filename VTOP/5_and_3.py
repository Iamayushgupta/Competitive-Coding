number=int(input(''))
if number <= 8:
    print('Invalid input')


else:
    if number%5!=0:
        if number%3==1:
            p=number//3
            print("{} three's and 2 five's".format(p-3))
        if number%3==2:
            q=number//3
            print("{} three's and 1 five's".format(q-1))

        if number%3==0:
            print("Only three's")

    elif number%5==0:
        if number%3==0:
            print("Only three's")

        else:
            print("Only five's")        