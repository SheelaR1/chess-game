class Piece():
    def __init__(self, color, position):
        self.color = color
        self.position = position
        self.has_moved = False

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
    def legal_moves(self, board):
        row, col = self.position 
        directions = [(1, 1), (1, -1), (-1, 1), (-1, -1)]
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
    def legal_moves(self, board):
        row, col = self.position
        directions = [(1, 1), (1, -1), (-1, 1), (-1, -1), (1, 0), (-1, 0), (0, 1), (0, -1)]
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
             
class Pawn(Piece):
    char = "P"
    def legal_moves(self, board):
        row, col = self.position
        moves = []
        if self.color == "w":
            direction = -1
            start_row = 6
        else:
            direction = 1
            start_row = 1
        new_row = row + direction
        new_col = col 
        if 0 <= new_row <= 7 and 0 <= new_col <= 7:
            target = board[new_row][new_col]
            if target is None:
                moves.append((new_row, new_col)) 
                if row == start_row and board[row + 2 * direction][col] is None:
                    moves.append((row + 2 * direction, col))
        # left - 1 , right + 1
        captures = [-1, 1]
        for offsets in captures:
            new_row = row + direction
            new_col = col + offsets
            if 0 <= new_row <= 7 and 0 <= new_col <= 7:
                target = board[new_row][new_col]
                if target is not None and target.color != self.color:
                    moves.append((new_row, new_col))
        return moves     
