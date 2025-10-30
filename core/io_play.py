from core.game_logic import calculate_hand_value

def ask_player_action() -> str:
    try:
        flage=True
        while flage:
            choice=input(f"\nPlease press your choice:\n H-Draw a card\n S-Stop, and pass the turn to the dealer")
            if choice =="h" or choice=="s":
                return choice


    except TypeError:
        print("\n The input is invalid")


def print_hands(player: dict, dealer: dict) -> None:
    print(f"valu_hand dealer: {calculate_hand_value(dealer["hand"])}")
    print(f"valu_hand player: {calculate_hand_value(player["hand"])}")


