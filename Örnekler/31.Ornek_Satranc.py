class Board:
    def __init__(self):
        self.board = [
            ["R", "N", "B", "Q", "K", "B", "N", "R"],
            ["P", "P", "P", "P", "P", "P", "P", "P"],
            [" ", ".", " ", ".", " ", ".", " ", "."],
            [".", " ", ".", " ", ".", " ", ".", " "],
            [" ", ".", " ", ".", " ", ".", " ", "."],
            [".", " ", ".", " ", ".", " ", ".", " "],
            ["p", "p", "p", "p", "p", "p", "p", "p"],
            ["r", "n", "b", "q", "k", "b", "n", "r"]
        ]
        self.current_turn = "W"
        self.moves = []

    def print_board(self):
        for row in self.board:
            print(" ".join(row))

    def get_piece(self, x, y):
        return self.board[x][y]

    def move_piece(self, start_x, start_y, end_x, end_y):
        piece = self.get_piece(start_x, start_y)

        if piece == " " or piece == ".":
            print("There is no piece at that position.")
            return False

        if self.get_piece(end_x, end_y).islower() and piece.isupper() or \
                self.get_piece(end_x, end_y).isupper() and piece.islower():
            if not self.validate_move(start_x, start_y, end_x, end_y):
                print("Invalid move. Try again.")
                return False

            self.board[start_x][start_y] = " "
            self.board[end_x][end_y] = piece
            self.moves.append(f"{piece}:{start_x}{start_y}->{end_x}{end_y}")
            return True
        else:
            print("Invalid move. Try again.")
            return False

    def validate_move(self, start_x, start_y, end_x, end_y):
        piece = self.get_piece(start_x, start_y)

        if piece.lower() == "p":
            return self.validate_pawn(start_x, start_y, end_x, end_y)
        elif piece.lower() == "r":
            return self.validate_rook(start_x, start_y, end_x, end_y)
        elif piece.lower() == "n":
            return self.validate_knight(start_x, start_y, end_x, end_y)
        elif piece.lower() == "b":
            return self.validate_bishop(start_x, start_y, end_x, end_y)
        elif piece.lower() == "q":
            return self.validate_queen(start_x, start_y, end_x, end_y)
        elif piece.lower() == "k":
            return self.validate_king(start_x, start_y, end_x, end_y)
        else:
            return False

    def validate_pawn(self, start_x, start_y, end_x, end_y):
            """
            Validates the move of a pawn from (start_x, start_y) to (end_x, end_y).
            """
            # Determine the color of the pawn based on its starting position
            color = self.board[start_x][start_y].color
            
            # Determine the direction in which the pawn can move based on its color
            direction = -1 if color == 'white' else 1
            
            # Check if the pawn is moving forward
            if end_x != start_x + direction:
                return False
            
            # Check if the pawn is moving diagonally to capture an opponent's piece
            if end_y == start_y + 1 or end_y == start_y - 1:
                target_piece = self.board[end_x][end_y]
                if target_piece is None or target_piece.color == color:
                    return False
                return True
            
            # Check if the pawn is moving forward by one or two squares
            if end_y == start_y:
                if end_x == start_x + direction:
                    target_piece = self.board[end_x][end_y]
                    if target_piece is not None:
                        return False
                    return True
                elif end_x == start_x + 2 * direction:
                    # Check if the pawn is moving two squares forward from its starting position
                    if start_x != 1 and start_x != 6:
                        return False
                    intermediate_piece = self.board[start_x + direction][start_y]
                    target_piece = self.board[end_x][end_y]
                    if intermediate_piece is not None or target_piece is not None:
                        return False
                    return True
            
            return False
    def validate_knight(self, start_x, start_y, end_x, end_y):
        """
        Validate if a knight can move from the starting position to the ending position
        """
        # Check if the ending position is not occupied by the player's own piece
        if self.board[end_x][end_y] is not None and self.board[end_x][end_y].color == self.current_turn:
            return False

        # Check if the move is a valid knight move
        x_diff = abs(end_x - start_x)
        y_diff = abs(end_y - start_y)
        if (x_diff == 1 and y_diff == 2) or (x_diff == 2 and y_diff == 1):
            return True

        return False

    def play(self):
        """
        Start the chess game and allow players to make moves until one player wins or there is a draw
        """
        print("Starting game...\n")
        self.print_board()

        while not self.game_over:
            start = input("\n{}'s turn. Enter move (e.g. 'a2 a4'): ".format(self.current_turn)).strip()
            end = input("Enter end position: ").strip()

            # Validate the move and make the move if valid
            if self.validate_move(start, end):
                self.make_move(start, end)
                self.print_board()

class Board:
    def __init__(self):
        self.board = [['-' for _ in range(8)] for _ in range(8)]
        self.white_king_pos = (7, 4)
        self.black_king_pos = (0, 4)
        self.moves_played = []
        self.game_over = False
        self.white_pieces = []
        self.black_pieces = []
        self.turn = 'white'
        self.setup_board()

    def setup_board(self):
        # White pieces
        self.board[7][0] = Rook('white')
        self.white_pieces.append(self.board[7][0])
        self.board[7][1] = Knight('white')
        self.white_pieces.append(self.board[7][1])
        self.board[7][2] = Bishop('white')
        self.white_pieces.append(self.board[7][2])
        self.board[7][3] = Queen('white')
    
        self.white_pieces.append(self.board[7][3])
        self.board[7][4] = King('white')
        self.white_pieces.append(self.board[7][4])
        self.board[7][5] = Bishop('white')
        self.white_pieces.append(self.board[7][5])
        self.board[7][6] = Knight('white')
        self.white_pieces.append(self.board[7][6])
        self.board[7][7] = Rook('white')
        self.white_pieces.append(self.board[7][7])
        for i in range(8):
            self.board[6][i] = Pawn('white')
            self.white_pieces.append(self.board[6][i])

        # Black pieces
        self.board[0][0] = Rook('black')
        self.black_pieces.append(self.board[0][0])
        self.board[0][1] = Knight('black')
        self.black_pieces.append(self.board[0][1])
        self.board[0][2] = Bishop('black')
        self.black_pieces.append(self.board[0][2])
        self.board[0][3] = Queen('black')
        self.black_pieces.append(self.board[0][3])
        self.board[0][4] = King('black')
        self.black_pieces.append(self.board[0][4])
        self.board[0][5] = Bishop('black')
        self.black_pieces.append(self.board[0][5])
        self.board[0][6] = Knight('black')
        self.black_pieces.append(self.board[0][6])
        self.board[0][7] = Rook('black')
        self.black_pieces.append(self.board[0][7])
        for i in range(8):
            self.board[1][i] = Pawn('black')
            self.black_pieces.append(self.board[1][i])

    def validate_move(self, start_x, start_y, end_x, end_y):
        piece = self.board[start_x][start_y]
        if not piece:
            return False
        if piece.color != self.turn:
            return False
        return piece.is_valid_move(start_x, start_y, end_x, end_y, self.board)

    def move_piece(self, start_pos, end_pos):
        start_x, start_y = start_pos
        end_x, end_y = end_pos

        # check if start and end positions are within the board
        if not self.is_valid_position(start_x, start_y) or not self.is_valid_position(end_x, end_y):
            print("Invalid move. Try again.")
            return

        # get the piece object at the starting position
        piece = self.board[start_x][start_y]

        # check if there is a piece at the starting position
        if piece is None:
            print("No piece at starting position. Try again.")
            return

        # check if the move is valid for the piece
        if not piece.is_valid_move(start_x, start_y, end_x, end_y):
            print("Invalid move for the selected piece. Try again.")
            return

        # check if the destination is occupied by a piece of the same color
        if self.board[end_x][end_y] is not None and self.board[end_x][end_y].color == piece.color:
            print("Destination position is occupied by your own piece. Try again.")
            return

        # move the piece to the destination
        self.board[start_x][start_y] = None
        self.board[end_x][end_y] = piece

        # update the piece's position attribute
        piece.position = end_pos

        # switch the turn to the other player
        self.turn = 'black' if self.turn == 'white' else 'white'

        # print the updated board
        self.print_board()
      


