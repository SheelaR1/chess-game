# Chess with Capture Minigames

A rules-complete chess game built from scratch in Python and Pygame. Captures aren't automatic: each one triggers a minigame, and the capture only succeeds if the attacker wins. A failed capture costs the attacker their turn.

## Features

- Full chess rules: legal move generation, check, checkmate, stalemate, castling, en passant, and pawn promotion
- Click-to-move interface with legal-move indicators and check highlighting
- Capture minigames, chosen at random:
  - **Rock Paper Scissors** against the computer
  - **Blackjack** against a dealer who draws to 17
- Object-oriented design with a shared minigame interface, so new games plug in without changes to the chess engine

## Getting Started

Requires Python 3.10+ and Pygame.

```bash
git clone https://github.com/SheelaR1/chess-game.git
cd chess-game
pip install pygame
python main.py
```

## Project Structure

| File | Purpose |
|---|---|
| `main.py` | Entry point |
| `chess.py` | Board state, game loop, move validation, and game-end detection |
| `pieces.py` | Piece classes and movement rules |
| `minigames.py` | Capture minigames |
| `images/` | Piece sprites |

## Roadmap

- [x] Chess engine with full rules
- [x] Rock Paper Scissors minigame
- [x] Blackjack minigame
- [ ] AI opponent
- [ ] Result screen after each minigame
- [ ] Draw rules (insufficient material, threefold repetition, fifty-move rule)
- [ ] Online multiplayer
- [ ] Connect Four minigame