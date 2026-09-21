import pygame
import random

# Card Gen
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

# Rock Paper Scissors
class RPS():

    def __init__(self, from_square, to_square):
        self.from_square = from_square
        self.to_square = to_square
        self.player_choice = None
        self.computer_choice = None
        self.result = None

    def draw(self, screen, font):
        pygame.draw.rect(screen, (30, 30, 30), (0, 0, 800, 800))
        # Rock 
        pygame.draw.rect(screen, (128, 128, 128), (100, 350, 100, 100))
        rock = font.render("Rock", True, (0, 0, 0))
        screen.blit(rock, (115, 385))
        # Paper
        pygame.draw.rect(screen, (240, 240, 240), (350, 350, 100, 100))
        paper = font.render("Paper", True, (0, 0, 0))
        screen.blit(paper, (360, 385))
        # Scissors
        pygame.draw.rect(screen, (200, 50, 50), (600, 350, 120, 100))
        scissors = font.render("Scissors", True, (0, 0, 0))
        screen.blit(scissors, (600, 385))

    def handle_click(self, pos):
        clicked = False
        x, y = pos 
        # Safe guarding against multiple clicks
        if self.result is not None:
            return
        # Choice handler
        if 100 <= x <= 200 and 350 <= y <= 450:
            self.player_choice = "rock"
            clicked = True
        elif 350 <= x <= 450 and 350 <= y <= 450:
            self.player_choice = "paper"
            clicked = True
        elif 600 <= x <= 720 and 350 <= y <= 450:
            self.player_choice = "scissors"
            clicked = True
        if clicked:
            self.computer_choice = random.choice(["rock", "paper", "scissors"])
            beats = {"rock": "scissors", "paper": "rock", "scissors": "paper"}
            if self.player_choice == self.computer_choice:
                self.result = "tie"
            elif beats[self.player_choice] == self.computer_choice:
                self.result = "win"
            else:
                self.result = "lose"
            print(self.result)

# BlackJack
class BJ():

    def __init__(self, from_square, to_square):
            self.from_square = from_square
            self.to_square = to_square
            self.font = pygame.font.SysFont('Times New Roman', 32)
            self.new_round()
            self.hit_button = pygame.Rect(100, 400, 150, 60)
            self.stand_button = pygame.Rect(600, 400, 150, 60)
    
    def new_round(self):
        self.deck = build_deck()
        self.player_hand = [self.deck.pop(), self.deck.pop()]
        self.dealer_hand = [self.deck.pop(), self.deck.pop()]
        self.round_over = False
        self.result = None

    def draw(self,screen, font):
        pygame.draw.rect(screen, (30, 30, 30), (0, 0, 800, 800))
        # Display Player Hand
        string = f"{self.player_hand} {hand_value(self.player_hand)}"
        draw_player_hand = self.font.render(string, True, (255, 255, 255))
        player_rect = draw_player_hand.get_rect(center=(400, 600))
        screen.blit(draw_player_hand, player_rect)
        # Display Dealer Hand
        if self.round_over:
            d_string = f"{self.dealer_hand} {hand_value(self.dealer_hand)}"
        else:
            d_string = f"[{self.dealer_hand[0]}, ??] ??"
        draw_dealer_hand = self.font.render(d_string, True, (255, 255, 255))
        dealer_rect = draw_dealer_hand.get_rect(center=(400, 200))
        screen.blit(draw_dealer_hand, dealer_rect)
        # Display Hit
        pygame.draw.rect(screen, (96, 209, 128), self.hit_button)
        hit = self.font.render("Hit", True, (255, 255, 255))
        screen.blit(hit, (self.hit_button.x +10, self.hit_button.y +10))
        # Display Stand
        pygame.draw.rect(screen, (235, 49, 49), self.stand_button)
        stand = self.font.render("Stand", True, (255, 255, 255))
        screen.blit(stand, (self.stand_button.x +10, self.stand_button.y +10))

    def handle_click(self, pos):
        # Check if game over
        if self.round_over:
            return
        # Handle hitting player hand
        if self.hit_button.collidepoint(pos):
            self.player_hand.append(self.deck.pop())
            if hand_value(self.player_hand) > 21:
                self.round_over = True
                self.result = "lose"
        #Handle Stand for player hand
        if self.stand_button.collidepoint(pos):
            while hand_value(self.dealer_hand) < 17:
                self.dealer_hand.append(self.deck.pop())
            self.round_over = True 
            # Blackjack win/lose logic 
            if hand_value(self.dealer_hand) > 21:
                self.result = "win"
            elif hand_value(self.player_hand) < hand_value(self.dealer_hand):
                self.result = "lose"
            elif hand_value(self.player_hand) > hand_value(self.dealer_hand):
                self.result = "win"
            else:
                self.new_round()