import random 

def build_deck():
    ranks = ["2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "K", "Q", "A"]
    suits = ["hearts", "diamonds", "spades", "clubs"]
    deck = []
    for rank in ranks:
        for suit in suits:
            deck.append((rank, suit))
    random.shuffle(deck)
    return deck

def hand_value(hand):
    total = 0 
    aces = 0
    for card in hand:
        if card[0] == "A":
            total += 11
            aces += 1
        elif card[0] in  ["K", "Q" ,"J"]:
            total += 10
        else:
            total += int(card[0])

    while total > 21 and aces > 0:
        total -= 10
        aces -= 1
    return total


        
            