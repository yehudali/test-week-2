def calculate_hand_value(hand: list[dict]) -> int:
    value=0
    rank = [None,"A", "2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K"]
    for i in range (len(hand)):
        y=rank.index( (hand[i]["rank"]) )
        if y <= 10:
            value+=y
        else:
            value+=10
    return value



def deal_two_each(deck: list[dict], player: dict, dealer: dict) -> None:
    player["hand"].append(deck.pop())
    player["hand"].append(deck.pop())

    dealer["hand"].append(deck.pop())
    dealer["hand"].append(deck.pop())
    # הדפסת ערך הידיים של שנייהם
    print(f"valu_hand dealer: {calculate_hand_value(dealer["hand"])}")
    print(f"valu_hand player: {calculate_hand_value(player["hand"])}")






def dealer_play(deck: list[dict], dealer: dict) -> bool:
    while calculate_hand_value(dealer["hand"])< 17:
        dealer["hand"].append(deck.pop())

    if calculate_hand_value(dealer["hand"])>21:
        print(" פסילה  של דילר!")
        return False

    if calculate_hand_value(dealer["hand"])<22:
        print("הדילר סיים")
        return True



def player_move(deck: list[dict], player: dict) -> bool:
    player["hand"].append(deck.pop())
    print(f"valu_hand player: {calculate_hand_value(player["hand"])}")

    if calculate_hand_value(player["hand"])>21:
        print("Disqualified! (return FALSE)")
        return False
    else:
        print("victory! (return True)")
        return True



def compare_the_players(player: dict, dealer: dict):
    d=calculate_hand_value(dealer["hand"])
    p=calculate_hand_value(player["hand"])
    if d>p:
        print("Dealer won")
    elif p>d:
        print("player won")
    else:
        print("draw!")

