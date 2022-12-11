def select_mod(first_player: str) ->str:
    n = int(input(f'{first_player} if you want to play alone -> press 1, if you play with your freand -> press 2: '))
    if n == 2:
        second_player = input("write your friend's name: ")
        print(f'Hello, {second_player}')    
    else: 
        bot_mod = int(input(f'{first_player} select the bot level, if low -> press 1, if high -> press 2: '))
        if bot_mod == 1:
            second_player = 'low_bot'
        else: second_player = 'high_bot'
    return second_player


def menu() -> str:
    print("MAIN MENU: \n"
            "1 - Single player\n"
            "2 - Multi player\n"            
            "3 - Exit")
    result = input('Select a menu item: ')
    return result


def sub_menu() -> str:
    print("SINGLE PLAYER MENU: \n"
            "1 - Low bot\n"
            "2 - Hight bot\n"            
            "3 - Exit")
    result = input('Select a menu item: ')
    return result


def first_player() -> str:
    first_player = input('Hello, what is yoir name: ')
    return first_player


def second_player() -> str:
    second_player = input('Hello Second player, what is yoir name: ')
    return second_player