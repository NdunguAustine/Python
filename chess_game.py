class ChessGame:
    def __init__(self):
        self.board = [
            ["rook", "knight", "bishop", "queen", "king", "bishop", "knight", "rook"],
            ["pawn", "pawn", "pawn", "pawn", "pawn", "pawn", "pawn", "pawn"],
            [" ", " ", " ", " ", " ", " ", " ", " "],
            [" ", " ", " ", " ", " ", " ", " ", " "],
            [" ", " ", " ", " ", " ", " ", " ", " "],
            [" ", " ", " ", " ", " ", " ", " ", " "],
            ["pawn", "pawn", "pawn", "pawn", "pawn", "pawn", "pawn", "pawn"],
            ["rook", "knight", "bishop", "queen", "king", "bishop", "knight", "rook"]
        ]
        self.selected_piece = None
        self.turn = "white"

    def select_piece(self, row, col):
        if self.turn == self.board[row][col].split(" ")[1]:
            self.selected_piece = (row, col)
        else:
            print("Not your turn.")

    def move_piece(self, row, col):
        if self.selected_piece:
            if self.is_valid_move(self.selected_piece, (row, col)):
                self.board[row][col] = self.board[self.selected_piece[0]][self.selected_piece[1]]
                self.board[self.selected_piece[0]][self.selected_piece[1]] = " "
                self.selected_piece = None
                self.turn = "black" if self.turn == "white" else "white"
            else:
                print("Invalid move.")
        else:
            print("No piece selected.")

    def is_valid_move(self, src, dest):
        piece = self.board[src[0]][src[1]].split(" ")[0]
        if piece == "pawn":
            return self.is_valid_pawn_move(src, dest)
        elif piece == "rook":
            return self.is_valid_rook_move(src, dest)
        elif piece == "knight":
            return self.is_valid_knight_move(src, dest)
        elif piece == "bishop":
            return self.is_valid_bishop_move(src, dest)
        elif piece == "queen":
            return self.is_valid_queen_move(src, dest)
        elif piece == "king":
            return self.is_valid_king_move(src, dest)

    def is_valid_pawn_move(self, src, dest):
        # Pawn rules: move one square forward or diagonally capture
        # (src, dest) represents (row, col) coordinates of the piece to be moved
        row_diff = dest[0] - src[0]
        col_diff = dest[1] - src[1]
        return (abs(row_diff) == 1 and abs(col_diff) == 1) or (abs(row_diff) == 2 and abs(col_diff) == 0)

    def is_valid_rook_move(self, src, dest):
        # Rook rules: move horizontally or vertically
        row_diff = dest[0] - src[0]
        col_diff = dest[1] - src[1]
        return (row_diff == 0 and col_diff != 0) or (row_diff != 0 and col_diff == 0)

    def is_valid_knight_move(self, src, dest):
        # Knight rules: move in L shape (two squares vertically and one square horizontally, or vice versa)
        row_diff = dest[0] - src[0]
        col_diff = dest[1] - src[1]
        return (abs(row_diff) == 2 and abs(col_diff) == 1) or (abs(row_diff) == 1 and abs(col_diff))