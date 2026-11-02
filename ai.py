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
    # Use a score system so the computer decides to capture pieces 
    best_score = -1
    best_moves = []
    for move in moves:
        from_square, to_square = move
        # unrequred as its not used
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

def evaluate(chess, color):
    score = 0 
    for row in range(8):
        for col in range(8):
            piece = chess.grid[row][col]
            # Skip empty square(no pieces there for points)
            if piece is None:
                continue
            piece_value = PIECE_VALUES[piece.char]
            if piece.color == color:
                score += piece_value
            else:
                score -= piece_value
    return score

def make_move(chess, move):
    # Spilt move into start and end square
    from_square, to_square = move
    old_row, old_col = from_square
    row, col = to_square
    piece = chess.grid[old_row][old_col]
    # Store target square
    captured = chess.grid[row][col]
    # Move the piece
    chess.grid[row][col] = piece
    chess.grid[old_row][old_col] = None
    # Piece calculate move from .position
    piece.position = (row,col)
    return captured

def undo_move(chess, move, captured):
    # Spilt move into start and end square
    from_square, to_square = move
    old_row, old_col = from_square
    row, col = to_square
    # Get the piece
    piece = chess.grid[row][col]
    # Move to original
    chess.grid[old_row][old_col] = piece
    chess.grid[row][col] = captured
    piece.position = (old_row, old_col)

def minimax(chess, depth, maximizing, ai_color):
    # Score the board as is 
    if depth == 0: 
        return evaluate(chess, ai_color)
    # Figure out whose turn it is at this level of search
    if maximizing:
        color = ai_color
    else:
        color = "b" if ai_color == "w" else "w"
    moves = all_moves(chess, color)
    # No legal move remaining
    if not moves:
        return evaluate(chess, ai_color)
    # AI Turn 
    if maximizing:
        best = float("-inf")
        for move in moves:
            captured = make_move(chess, move)
            score = minimax(chess, depth - 1, False, ai_color)
            undo_move(chess, move, captured)
            if score > best:
                best = score
        return best
    # During Player Turn 
    else:
        best = float("inf")
        for move in moves: 
            captured = make_move(chess, move)
            score = minimax(chess, depth -1, True, ai_color)
            undo_move(chess, move, captured)
            if score < best:
                best = score
        return best

def minimax_move(chess, color):
    moves = all_moves(chess, color)
    if not moves:
        return None
    best_score = float("-inf")
    best_moves = []
    for move in moves:
        captured = make_move(chess, move)
        score = minimax(chess, 1, False, color)
        undo_move(chess, move, captured)
        if score > best_score:
            best_score = score
            best_moves = [move]
        elif score == best_score:
            best_moves.append(move)
    return random.choice(best_moves)