import pygame
import sys

class Chess():
    def __init__(self):
        pygame.init()
        width = 800
        height = 800
        self.screen = pygame.display.set_mode((width, height))
        pygame.display.set_caption("Chess Game")
        self.clock = pygame.time.Clock()
        self.board_setup()

    def run(self):
        running = True 
        while running: 
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False     
            self.screen.fill((0,0,0))
            self.draw_board()
            self.draw_pieces()
            pygame.display.flip()
            self.clock.tick(60)

        

        pygame.quit()

    def draw_board(self):
        for row in range(8):
            for column in range(8):
                y = row * 100
                x = column * 100
                if (row + column) % 2 == 0:
                    color = (235, 235, 210)
                else:
                    color = (120, 80, 60)
                pygame.draw.rect(self.screen, color, (x, y, 100, 100))

    def board_setup(self):
        grid = [[None for _ in range(8)] for _ in range(8)] 
        self.grid = grid
        for col in range(8):
            self.grid[1][col] = Pawn("b", (1, col))
            self.grid[6][col] = Pawn("w", (6, col))
        back_row = [Rook, Knight, Bishop, Queen, King, Bishop, Knight, Rook]
        for col in range(len(back_row)):
            self.grid[0][col] = back_row[col]("b", (0, col))
            self.grid[7][col] = back_row[col]("w", (7, col))
        
        

    def draw_pieces(self):
        for row in range(8):
            for col in range(8):
                piece = self.grid[row][col]
                if piece is not None:
                    image = "images/" + piece.color + piece.char + ".png"
                    image= pygame.image.load(image)
                    image= pygame.transform.smoothscale(image, (100, 100))
                    self.screen.blit(image, (col * 100, row * 100))
            
            
    

    def special_moves():
        pass

class Piece():
    def __init__(self, color, position):
        self.color = color
        self.position = position


    def legal_moves(self):
        pass

class Knight(Piece):
    char = "N"
    def legal_moves(self, board):
        offsets = [(2, 1), (1, 2), (-1, 2), (1, -2), (-1, -2), (-2, -1), (-2, 1), (2, -1)]
        row, col = self.position
        moves = []
        # dr = delta row , dc = detla column 
        for dr, dc in offsets:
            new_row = row + dr 
            new_col = col + dc

            if 0 <= new_row <= 7 and 0 <= new_col <=7:
                target = board[new_row][new_col]
                if target is None or target.color != self.color:
                    moves.append((new_row, new_col)) 
        return moves


        

class Rook(Piece):
    char = "R"
    def legal_moves(self, board):
        row, col = self.position
        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        moves = []
        for dr, dc in directions:
            new_row = row + dr
            new_col = col + dc
            while 0 <= new_row <= 7 and 0 <= new_col <= 7:
                target = board[new_row][new_col]

                if target is None:
                    moves.append((new_row, new_col))
                    new_row += dr
                    new_col += dc
                else:
                    if target.color != self.color:
                        moves.append((new_row, new_col)) 
                    break
        return moves

class Bishop(Piece):
    char = "B"
    def legal_moves():
        pass

class King(Piece):
    char = "K"
    def legal_moves(self, board):
        offsets = [(1, 0), (0, 1), (-1, 0), (0, -1), (1, 1), (1, -1), (-1, 1), (-1, -1)]
        row, col = self.position
        moves = []
        #delta row delta col
        for dr, dc in offsets:
            new_row = row + dr
            new_col = col + dc

            if 0 <= new_row <= 7 and 0 <= new_col <= 7:
                target = board[new_row][new_col]
                if target is None or target.color != self.color:
                     moves.append((new_row, new_col)) 
        return moves


class Queen(Piece):
    char = "Q"
    def legal_moves():
        pass

class Pawn(Piece):
    char = "P"
    def legal_moves():
        pass




if __name__ == "__main__":
    game = Chess()
    rook = game.grid[4][4] = Rook("w", (4,4))
    print(rook.legal_moves(game.grid))
    game = Chess()
    game.run()
    



