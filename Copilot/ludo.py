class LudoGame:
    def __init__(self):
        # Initialize the game board with 0s
        self.board = [0] * 52

        # Initialize the pieces at the starting position
        self.piece_position = [[0, 0, 0, 0], [0, 0, 0, 0]]  # [player1's pieces, player2's pieces]

    def move_piece(self, player, piece, steps):
        # Move the piece the given number of steps
        self.piece_position[player][piece] += steps

        # Check if the piece has moved off the end of the board
        self.check_board_bounds(player, piece)

        # Check if the player's piece has landed on the opponent's piece
        self.check_capture(player, piece)

        # Update the board
        self.board[self.piece_position[player][piece]] = player + 1

    def check_board_bounds(self, player, piece):
        # If the piece has moved off the end of the board, wrap it around
        if self.piece_position[player][piece] >= len(self.board):
            self.piece_position[player][piece] -= len(self.board)

    def check_capture(self, player, piece):
        # Get the opponent's index
        opponent = 1 - player  
        for opp_piece in range(4):
            if self.piece_position[player][piece] == self.piece_position[opponent][opp_piece]:
                # The player has captured the opponent's piece
                print(f"Player {player + 1} has captured Player {opponent + 1}'s piece {opp_piece + 1}!")
                # Send the opponent's piece back to the start
                self.piece_position[opponent][opp_piece] = 0

    def print_board(self):
        # Print the current state of the board
        for i in range(len(self.board)):
            print(self.board[i], end=' ')
        print()

# Create a new game
game = LudoGame()

# Move the pieces
game.move_piece(0, 0, 3)  # Player 1 moves piece 1, 3 steps
game.move_piece(1, 0, 3)  # Player 2 moves piece 1, 3 steps, capturing Player 1's piece

# Print the board
game.print_board()