def user_choice():
    choice='wrong'
    accept=range(0,11)
    bool=False
    while choice.isdigit()==False:
        choice=input('please enter a number (0-10)')

        if choice.isdigit()==False:
            print('sorry it is not a digit')
        else:
            if int(choice) in accept:
                bool=True
            else:
                return "sorry you are out of range"
                

    return int(choice)
print(user_choice())
