class ChessBoard:
    def __init__(self):
        self.board = [[None for _ in range(8)] for _ in range(8)]
        self.create_starting_board()

    def create_starting_board(self):
        self.board[0][0] = Rook("black")
        self.board[0][1] = Knight("black")
        self.board[0][2] = Bishop("black")
        self.board[0][3] = Queen("black")
        self.board[0][4] = King("black")
        self.board[0][5] = Bishop("black")
        self.board[0][6] = Knight("black")
        self.board[0][7] = Rook("black")
        self.board[1][0] = Pawn("black")
        self.board[1][1] = Pawn("black")
        self.board[1][2] = Pawn("black")
        self.board[1][3] = Pawn("black")
        self.board[1][4] = Pawn("black")
        self.board[1][5] = Pawn("black")
        self.board[1][6] = Pawn("black")
        self.board[1][7] = Pawn("black")
        self.board[7][0] = Rook("white")
        self.board[7][1] = Knight("white")
        self.board[7][2] = Bishop("white")
        self.board[7][3] = Queen("white")
        self.board[7][4] = King("white")
        self.board[7][5] = Bishop("white")
        self.board[7][6] = Knight("white")
        self.board[7][7] = Rook("white")
        self.board[6][0] = Pawn("white")
        self.board[6][1] = Pawn("white")
        self.board[6][2] = Pawn("white")
        self.board[6][3] = Pawn("white")
        self.board[6][4] = Pawn("white")
        self.board[6][5] = Pawn("white")
        self.board[6][6] = Pawn("white")
        self.board[6][7] = Pawn("white")

    def get_piece(self, position):
        x, y = position
        return self.board[x][y]

    def set_piece(self, position, piece):
        x, y = position
        self.board[x][y] = piece

    def remove_piece(self, position):
        x, y = position
        self.board[x][y] = None
    def remove_piece(self, position):
        x, y = position
        self.board[x][y] = None
class Piece:
    def __init__(self, color):
        self.color = color
        self.symbol = None

    def can_move(self, start, end, board):
        raise NotImplementedError()


class Pawn(Piece):
    def __init__(self, color):
        super().__init__(color)
        self.symbol = "♟" if color == "black" else "♙"

    def can_move(self, start, end, board):
        start_x, start_y = start
        end_x, end_y = end
        direction = -1 if self.color == "black" else 1
        if end_x == start_x + direction and end_y == start_y and board[end_x][end_y] is None:
            return True
        if (
            end_x == start_x + direction
            and abs(end_y - start_y) == 1
            and board[end_x][end_y] is not None
            and board[end_x][end_y].color != self.color
        ):
            return True
        if (
            start_x == 1
            and end_x == start_x + direction * 2
            and end_y == start_y
            and board[end_x][end_y] is None
            and board[start_x + direction][end_y] is None
        ):
            return True
        if (
            start_x == 6
            and end_x == start_x + direction * 2
            and end_y == start_y
            and board[end_x][end_y] is None
            and board[start_x + direction][end_y] is None
        ):
            return True
        return False


class Rook(Piece):
    def __init__(self, color):
        super().__init__(color)
        self.symbol = "♜" if color == "black" else "♖"

    def can_move(self, start, end, board):
        start_x, start_y = start
        end_x, end_y = end
        if start_x == end_x:
            step = -1 if start_y > end_y else 1
            for i in range(start_y + step, end_y, step):
                if board[start_x][i] is not None:
                    return False
            return True
        elif start_y == end_y:
            step = -1 if start_x > end_x else 1
            for i in range(start_x + step, end_x, step):
                if board[i][start_y] is not None:
                    return False
            return True
        return False


class Knight(Piece):
    def __init__(self, color):
        super().__init__(color)
        self.symbol = "♞" if color == "black" else "♘"

    def can_move(self, start, end, board):
        start_x, start_y = start
        end_x, end_y = end
        dx = abs(end_x - start_x)
        dy = abs(end_y - start_y)
        return dx * dy == 2 and board[end_x][end_y] is None

class Bishop(Piece):
    def __init__(self, color):
        super().__init__(color)
        self.symbol = "♝" if color == "black" else "♗"

    def can_move(self, start, end, board):
        start_x, start_y = start
        end_x, end_y = end
        dx = abs(end_x - start_x)
        dy = abs(end_y - start_y)
        if dx != dy:
            return False
        step_x = -1 if start_x > end_x else 1
        step_y = -1 if start_y > end_y else 1
        x, y = start_x + step_x, start_y + step_y
        while x != end_x and y != end_y:
            if board[x][y] is not None:
                return False
            x += step_x
            y += step_y
        return True
class Queen(Piece):
    def __init__(self, color):
        super().__init__(color)
        self.symbol = "♛" if color == "black" else "♕"

    def can_move(self, start, end, board):
        rook = Rook(self.color)
        bishop = Bishop(self.color)
        return rook.can_move(start, end, board) or bishop.can_move(start, end, board)


class King(Piece):
    def __init__(self, color):
        super().__init__(color)
        self.symbol = "♚" if color == "black" else "♔"

    def can_move(self, start, end, board):
        start_x, start_y = start
        end_x, end_y = end
        dx = abs(end_x - start_x)
        dy = abs(end_y - start_y)
        if dx <= 1 and dy <= 1 and board[end_x][end_y] is None:
            return True
        return False
class Game:
    def __init__(self):
        self.board = ChessBoard()
        self.current_player = "white"

    def switch_player(self):
        self.current_player = "black" if self.current_player == "white" else "white"

    def make_move(self, start, end):
        piece = self.board.get_piece(start)
        if piece is None:
            return False
        if piece.color != self.current_player:
            return False
        if not piece.can_move(start, end, self.board.board):
            return False
        self.board.set_piece(end, piece)
        self.board.remove_piece(start)
        self.switch_player()
        return True

    def print_board(self):
        for row in self.board.board:
            for square in row:
                print(square.symbol if square is not None else ".", end=" ")
            print()

    def play(self):
        print("Welcome to chess!")
        while True:
            print()
            print(f"It is {self.current_player}'s turn.")
            self.print_board()
            move = input("Enter your move (e.g. 'a2 a4'): ")
            start, end = move.split()
            start = (int(start[1]) - 1, ord(start[0]) - 97)
            end = (int(end[1]) - 1, ord(end[0]) - 97)
            if self.make_move(start, end):
                print("Move successful!")
            else:
                print("Invalid move. Try again.")
    
    def make_move(self, start, end):
        piece = self.board.get_piece(start)
        if piece is None or piece.color != self.current_player:
            return False
        if not piece.can_move(end, self.board):
            return False
        captured_piece = self.board.get_piece(end)
        self.board.remove_piece(end)
        self.board.move_piece(start, end)
        if self.board.is_check(self.current_player):
            self.board.undo_move(start, end, captured_piece, piece)
            return False
        self.moves.append((piece, start, end, captured_piece))
        self.current_player = "White" if self.current_player == "Black" else "Black"
        return True
    
game = Game()
game.play()
