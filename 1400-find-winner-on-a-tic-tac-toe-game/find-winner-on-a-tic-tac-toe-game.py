class Solution:
    def tictactoe(self, moves: List[List[int]]) -> str:
        # Initialize the board with empty cells
        board = [['' for _ in range(3)] for _ in range(3)]
        
        # Helper function to check for a winner
        def check_winner(player):
            # Check rows and columns
            for i in range(3):
                if all(board[i][j] == player for j in range(3)) or \
                   all(board[j][i] == player for j in range(3)):
                    return True
            # Check diagonals
            if all(board[i][i] == player for i in range(3)) or \
               all(board[i][2-i] == player for i in range(3)):
                return True
            return False
        
        # Fill the board based on moves
        for i, (x, y) in enumerate(moves):
            board[x][y] = 'A' if i % 2 == 0 else 'B'
        
        # Check if player A wins
        if check_winner('A'):
            return "A"
        # Check if player B wins
        if check_winner('B'):
            return "B"
        # Check if the game is still pending
        if len(moves) < 9:
            return "Pending"
        # Otherwise, it's a draw
        return "Draw"