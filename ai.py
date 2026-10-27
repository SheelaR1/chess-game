import random 
PIECE_VALUES = {"P": 1, "N": 3, "B": 3, "R": 5, "Q": 9, "K":0}


def random_moves(chess, color):
    moves = all_moves(chess, color)
    if not moves:
        return None
    else:
        return random.choice(moves)

def all_moves(chess, color):
    moves = []
    for row in range(8):
        for col in range(8):
            piece = chess.grid[row][col]
            if piece is None or piece.color != color:
                continue
            piece_moves = chess.get_legal_moves(piece)
            # Save where the piece is and where it goes
            for move in piece_moves:
                moves.append(((row,col) , move))
    return moves

def greedy_move(chess, color):
    moves = all_moves(chess, color)
    if not moves:
            return None
    best_score = -1
    best_moves = []
    for move in moves:
        from_square, to_square = move
        old_row, old_col = from_square
        row, col = to_square
        target = chess.grid[row][col]
        if target is None:
            score = 0
        else:
            score = PIECE_VALUES[target.char]
        if score > best_score:
            best_score = score
            best_moves = [move]
        elif score == best_score:
            best_moves.append(move)
    return random.choice(best_moves)

                
