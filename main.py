from core.deck import (build_standard_deck, shuffle_by_suit)
from core.game_logic import (calculate_hand_value,deal_two_each,dealer_play,player_move,compare_the_players)
from core.io_play import ask_player_action,print_hands


def run_full_game(deck, player, dealer):
    #חלוקה בין שניהם, והדפסת ערך היידים
    deal_two_each(deck, player, dealer)

    #תור שחקן
    flage = True
    while flage:
        usr_choice = ask_player_action()

        if usr_choice == "s":
            dealer_play(deck, dealer)
            print_hands(player, dealer)

        if usr_choice == "h":
            if not player_move(deck,player):
                flage = False

        compare_the_players(player, dealer)



if __name__ == "__main__":
    deck = build_standard_deck()
    shuffle_by_suit(deck,5000)

    player = {"hand": []}
    dealer = {"hand": []}

    run_full_game(deck, player, dealer)
