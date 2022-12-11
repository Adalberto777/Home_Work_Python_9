from colorama import init

from colorama import Fore, Back, Style
init()

from random import randint

# жеребьевка первого хода
def lottery(first_player: str, second_player: str) ->int:
    print("to find out which of you will walk first, let's draw lots")
    number_p_f = int(input(f'{first_player} Enter any number: ' ))

    if second_player == 'low_bot' or second_player == 'high_bot':
        number_p_s = randint(0, 100)
        print(f'The bot entered {number_p_s}')
    else:
        number_p_s = int(input(f'{second_player} Enter any number: ' ))

    lucky_num_p_f = randint(0, 100)
    lucky_num_p_s = randint(0, 100)

    if abs(number_p_f - lucky_num_p_f) > abs(number_p_s - lucky_num_p_s):
        print(f'The winner of the draw {first_player}, сongratulate')  
        n = 1      
    else: 
        print(f'The winner of the draw {second_player}, сongratulate')
        n = 2
    return n


# логика легкого бота
def low_bot_mod(total_candies: int, taken_candies_max: int) ->int:
    if total_candies > taken_candies_max:
        n = randint(1, taken_candies_max)
    else:
         n = total_candies
    return n


# логика тяжелого бота
def high_bot_mod(total_candies: int, taken_candies_max: int) ->int:
    if total_candies > taken_candies_max:
        n = total_candies % (taken_candies_max + 1)
        if n == 0:
            n = taken_candies_max
    else:
         n = total_candies
    return n


# игра с конфетами
def game(total_candies: int, first_player: str, second_player: str, winner_lottery: int, taken_candies_max: int) ->str:
    if winner_lottery == 2:
        temp = first_player
        first_player = second_player
        second_player = temp

    winner = ''
    while total_candies > 0:
        winner = first_player
        if first_player == 'low_bot':
            taken_candies = low_bot_mod(total_candies, taken_candies_max)
            print(Fore.GREEN + '  ')               
            print(f'The bot take candies the: {taken_candies}')
            print(Style.RESET_ALL)           
        elif first_player == 'high_bot':
            taken_candies = high_bot_mod(total_candies, taken_candies_max)
            print(Fore.GREEN + '  ')               
            print(f'The bot take candies the: {taken_candies}')
            print(Style.RESET_ALL)
        else:
            taken_candies = int(input(f"{first_player} Enter number of candies. It should be in range [1...28]: "))

        total_candies -= taken_candies
        print(f'There are some sweets left in the basket: {total_candies}')

        if total_candies > 0:
            winner = second_player
            if second_player == 'low_bot':
                taken_candies = low_bot_mod(total_candies, taken_candies_max)
                print(Fore.GREEN + ' ')               
                print(f'The bot take candies the: {taken_candies}')
                print(Style.RESET_ALL)                
            elif second_player == 'high_bot':
                taken_candies = high_bot_mod(total_candies, taken_candies_max)
                print(Fore.GREEN + ' ')               
                print(f'The bot take candies the: {taken_candies}')
                print(Style.RESET_ALL)
                             
            else:
                taken_candies = int(input(f"{second_player} Enter number of candies. It should be in range [1...28]: "))
            
        total_candies -= taken_candies
        print(f'There are some sweets left in the basket: {total_candies}')
    print(Back.BLUE + ' ')
    print(f'{winner} win, сongratulate')
    print(Style.RESET_ALL) 


# print(Fore.RED + 'some red text')
# print(Backprint(Style.RESET_ALL).BLUE + 'and with a green background')
# print(Style.DIM + 'and in dim text')
# 
# print('back to normal now')

