import view
import model_game

total_candies = 220
taken_candies_max = 28
first_player = view.first_player()


def get_menu_item() -> str:
    result_menu = view.menu()
    if result_menu == '1':
        result_sub_menu = view.sub_menu()
        if result_sub_menu == '1':
            second_player = 'low_bot' 
            winner_lottery = model_game.lottery(first_player, second_player)
            model_game.game(total_candies, first_player, second_player, winner_lottery, taken_candies_max)
        elif result_sub_menu == '2':
            second_player = 'high_bot'
            winner_lottery = model_game.lottery(first_player, second_player)
            model_game.game(total_candies, first_player, second_player, winner_lottery, taken_candies_max)
        elif result_sub_menu == '3':
            print("Good Bye!")
        else: 
            print("введен несуществующий пункт, выберите пункт меню от 1 до 8")
            view.sub_menu()
    elif result_menu == '2':
            second_player = view.second_player()
            winner_lottery = model_game.lottery(first_player, second_player)
            model_game.game(total_candies, first_player, second_player, winner_lottery, taken_candies_max)
    elif result_menu == '3': 
        print("Good Bye!") 
    else: 
        print("введен несуществующий пункт, выберите пункт меню от 1 до 8")
        get_menu_item()  