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

class BJ():

    def __init__(self):
        self.new_round()

    def new_round(self):
        self.deck = build_deck()
        self.player_hand = [self.deck.pop(), self.deck.pop()]
        self.dealer_hand = [self.deck.pop(), self.deck.pop()]
        self.round_over = False
        self.result = None

    def draw(self,screen):
        pass

if __name__ == "__main__":
    game = BJ()
    print(game.player_hand, hand_value(game.player_hand))
    print(game.dealer_hand, hand_value(game.dealer_hand))
    print(len(game.deck))
            