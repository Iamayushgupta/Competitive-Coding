game_list=[0,1,2]
def display_game(game_list):
    print('here is the game list: ')
    print(game_list)

display_game(game_list)

def position_choice():
    choice='wrong'
    while choice not in ['0','1','2']:
        choice=input("pick a position(0,1,2): ")
        if choice not in ['0','1','2']:
            print("sorry, invalid choice!")
    return int(choice)
print(position_choice())


def replacement_choice(game_list,position):
    user_placement=input("type a string to replace position: ")
    game_list[position]=user_placement
    return game_list
print(replacement_choice(game_list,1))


def gameon_choice():
    choice='wrong'
    while choice not in ['Y','N']:
        choice=input("keep playing?,(Y or N): ")
        if choice not in ['Y','N']:
            print("sorry, i dont understand!")
    if choice=='Y':
        return True
    else:
        return False

print(gameon_choice())

game_on=True
game_list=[0,1,2]
while game_on:
    display_game(game_list)
    position=position_choice()
    game_list=replacement_choice(game_list,position)
    display_game(game_list)
    game_on=gameon_choice()