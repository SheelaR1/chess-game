import random 

def random_moves(chess, color):
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
    if not moves:
        return None
    return random.choice(moves)


                
