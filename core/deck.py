import random
def build_standard_deck() -> list[dict]:  #->[{'rank': 'A', 'suite': 'H'}, {'rank': 'A', 'suite': 'C'}*52]
    deck=[]
    rank=["A","2","3","4","5","6","7","8","9","10","J","Q","K"]
    suite=["H","C","D","S"]
    for i in rank:
        for j in suite:
            deck.append({"rank":i, "suite":j})
    return deck


def shuffle_by_suit(deck: list[dict], swaps: int = 5000) -> list[dict]:

    for i in range(swaps):
        i = random.randint(0, len(deck)-1)
        j = random.randint(0, len(deck)-1)

        if deck[j]["suite"]=="H":
            while j % 5 !=0 and  i == j:
                i = random.randint(0, len(deck)-1)
                j = random.randint(0, len(deck)-1)
            deck[j],deck[i]=deck[i],deck[j]

        if deck[j]["suite"] == "C":
            while j % 3 != 0 and i == j:
                i = random.randint(0, len(deck)-1)
                j = random.randint(0, len(deck)-1)
            deck[j], deck[i] = deck[i], deck[j]

        if deck[j]["suite"] == "D":
            while j % 2 != 0 and i == j:
                i = random.randint(0, len(deck)-1)
                j = random.randint(0, len(deck)-1)
            deck[j], deck[i] = deck[i], deck[j]

        if deck[j]["suite"] == "S":
            while j % 7 != 0 and i == j:
                i = random.randint(0, len(deck)-1)
                j = random.randint(0, len(deck)-1)
            deck[j], deck[i] = deck[i], deck[j]





