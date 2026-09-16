import pygame
import random

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

    def __init__(self):
        pass

    def draw(self, screen, ):
        # Draw a hit button 

        # Draw a stand button

        # Animate 2 cards being drawn for your hand

        # Draw a card for the dealer one face one shown to the player
        pass

    def handle_click(self, pos):
        # safeguard against mutiple clicks

        # unpack positon of x, y 
        # if player clicks hit make the computer deal another card and see if its 21 or less
        # if it more than 21 lose the game
        # if not and player stands and compares to computer 

        pass