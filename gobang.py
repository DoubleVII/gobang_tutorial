# coding=utf-8


class SuperPiece:
    def is_empty(self) -> bool:
        """
        Determine whether the piece is empty.

        Returns:
            bool: True if the piece is empty
        """
        raise NotImplementedError

    def is_black(self) -> bool:
        """
        Determine whether the piece is black.

        Returns:
            bool: True if the piece is black
        """
        raise NotImplementedError

    def is_white(self) -> bool:
        """
        Determine whether the piece is white.

        Returns:
            bool: True if the piece is white
        """
        raise NotImplementedError


class SuperChessboard:
    def __init__(self, size: int):
        """
        Initialization.

        Args:
            size (int): the length and width of the chessboard
        """
        self.size = size

    def get_board_size(self) -> int:
        """
        Get the chessboard size.

        Returns:
            int: the size of the chessboard
        """
        return self.size

    def set_piece(self, piece: SuperPiece, position: tuple) -> bool:
        """
        Set a given piece in a given position only if the position in the chessboard
        is empty.
        
        Args:
            piece (SuperPiece): the piece to be set
            position (tuple): the position to set the piece, with the form of (x,y), 
            x is the row index and y is the column index, which should large than 0,
            i.e. x,y is in [1, size]

        Returns:
            bool: True if the piece is set successfully; False is there is not empty
            in the given position.
        """
        raise NotImplementedError

    def set_black_piece(self, position: tuple) -> bool:
        """
        Set a black piece in a given position only if the position in the chessboard
        is empty.
        
        Args:
            position (tuple): the position to set the piece, with the form of (x,y), 
            x is the row index and y is the column index, which should large than 0,
            i.e. x,y is in [1, size]

        Returns:
            bool: True if the piece is set successfully; False is there is not empty
            in the given position.
        """
        raise NotImplementedError

    def set_white_piece(self, position: tuple) -> bool:
        """
        Set a white piece in a given position only if the position in the chessboard
        is empty.
        
        Args:
            position (tuple): the position to set the piece, with the form of (x,y), 
            x is the row index and y is the column index, which should large than 0,
            i.e. x,y is in [1, size]

        Returns:
            bool: True if the piece is set successfully; False is there is not empty
            in the given position.
        """
        raise NotImplementedError

    def set_empty_piece(self, position: tuple):
        """
        Set a empty piece in a given position.
        
        Args:
            position (tuple): the position to set the piece, with the form of (x,y), 
            x is the row index and y is the column index, which should large than 0,
            i.e. x,y is in [1, size]
        """
        raise NotImplementedError

    def get_piece(self, position: tuple) -> SuperPiece:
        """
        Get the piece in the given position.

        Args:
            position (tuple): querying position, with the form of (x,y), 
            x is the row index and y is the column index, which should large than 0,
            i.e. x,y is in [1, size]

        Returns:
            SuperPiece: the piece in the given position
        """
        raise NotImplementedError

    def isEmpty(self, position: tuple) -> bool:
        """
        Determine whether the position in the chessboard is empty.

        Args:
            position (tuple): querying position, with the form of (x,y), 
            x is the row index and y is the column index, which should large than 0,
            i.e. x,y is in [1, size]

        Returns:
            bool: True if the piece in the given position is empty
        """
        raise NotImplementedError


class SuperGame:
    def __init__(self):
        """
        Initialization. We have initialized the `display` and `round_num`, but left the
        `board_size` and `board` uninitialized.
        """
        self.display = Display()
        self.round_num = 1

        # ???????????????????????????
        self.board_size = 0
        self.board = None

    def start(self):
        """
        Start the game.
        """
        self.game_loop()

    def show_board(self):
        """
        Show current chessboard to the user.
        """
        self.display.display_board(self.board)

    def game_loop(self):
        """
        Start the game main loop.
        In this function, you should first call the `self.display.display_help_info()`,
        then enter a for/while loop, in which you should do things bellow:
            1. update `self.round_num`.
            2. diaplsy current round info by calling `self.display.display_round`.
            3. display chessboard by calling `super().show_board()`.
            4. get position input by calling `self.display.input_position()`.
                4.1. call `self.display.display_position_empty_error()` if there
                is not empty in the position.
                4.2. call `self.display.display_position_boundary_error()` if the
                position exceeds the boundary.
                4.3. call `self.display.display_position_info(position, self.black_turn)` if
                the position is valid.
            5. set a black/white piece in the input position.
            6. break loop if black/white wins the game.
        """
        raise NotImplementedError

    def win_judging(self) -> bool:
        """
        Determine whether black/white wins the game.

        Returns:
            bool: True if black/white wins the game
        """
        raise NotImplementedError


class Display:
    def __init__(self, gbk_console=False, ascii_piece=False):
        """
        Initialization.

        Args:
            gbk_console (bool): use gbk encoding, if your program outputs messy code, you
            can try it.
        """
        import sys
        import io

        sys.stdout = io.TextIOWrapper(
            sys.stdout.buffer, encoding="gbk" if gbk_console else "utf-8"
        )

        self.balck_unit = "???"  if not ascii_piece else "x"
        self.white_unit = "???"  if not ascii_piece else "o"
        self.empty_unit = "+"

    def input_board_size(self) -> int:
        """
        Get chessboard size from user.

        Returns:
            int: the size of the chessboard
        """
        self.info("?????????????????????:")
        size = int(input())
        return size

    def input_position(self) -> tuple:
        """
        Get next position from user to set a piece.

        Returns:
            tuple: the position tuple, with the form of (x,y), x is the row index
            and y is the column index, which should large than 0, i.e. x,y is in [1, size]
        """
        self.info("???????????????:")
        position = tuple(map(int, input().split()))
        while True:
            if len(position) == 2:
                break
            self.info("????????????????????????", True)
            self.info("???????????????:")
            position = tuple(map(int, input().split()))
        return position

    def info(self, message: str, space_line=False):
        """
        Print a message to user.

        Args:
            message (str): the message string to print
            space_line (bool): whether to print another '\n' after the message
        """
        print(message)
        if space_line:
            print("")

    def display_winner(self, black_win: bool):
        """
        Print game winner info.

        Args:
            black_win (bool): wether the winner is black
        """
        win_message = "{}?????????".format("???" if black_win else "???")
        self.info(win_message, True)

    def display_round(self, round_num, black_turn: bool):
        """
        Print round info.

        Args:
            round_num (int): current round
            black_turn (bool): wether the round is black's round
        """
        self.split_line(20)
        round_message = "??????{} {}?????????:".format(round_num, "???" if black_turn else "???")
        self.info(round_message, True)

    def display_position_info(self, position: tuple, black_turn: bool):
        """
        Print the input position info of this round.

        Args:
            position (tuple): the input position of this round, with the form of (x,y), 
            x is the row index and y is the column index, which should large than 0,
            i.e. x,y is in [1, size]
            black_turn (bool): wether the round is black's round
        """
        position_info = "{}?????????????????? ({} {})".format(
            "???" if black_turn else "???", position[0], position[1]
        )
        self.info(position_info, True)

    def display_help_info(self):
        """
        Print help message.
        """
        title = "????????????:"
        position_info = '??????????????????"3 5"????????????3??????5???????????????1???????????????????????????????????????'
        self.info(title)
        self.info(position_info, True)

    def display_position_boundary_error(self):
        """
        Print position boundary error message.
        """
        self.info("???????????????????????????", True)

    def display_position_empty_error(self):
        """
        Print position empty error message.
        """
        self.info("???????????????????????????", True)

    def split_line(self, width):
        """
        Print `--` for width times.
        """
        print("--" * width)

    def display_board(self, chessboard: SuperChessboard):
        """
        Display chessboard.

        Args:
            chessboard (SuperChessboard): the chessboard to display
        """
        board_size = chessboard.get_board_size()
        self.split_line(board_size + 1)
        # print coordinate
        row_str = "{:<2}" * board_size
        print("  " + row_str.format(*list(range(1, board_size + 1))))

        for i in range(1, board_size + 1):
            board_row = []
            for j in range(1, board_size + 1):
                piece = chessboard.get_piece((i, j))
                if piece.is_empty():
                    board_row.append(self.empty_unit)
                elif piece.is_white():
                    board_row.append(self.white_unit)
                else:
                    board_row.append(self.balck_unit)
            row_str = "{:<2d}".format(i) + " ".join(board_row)
            print(row_str)
        self.split_line(board_size + 1)


# your code here
# class Piece(SuperPiece) ...
# class Chessboard(SuperChessboard) ...
# class Game(SuperGame) ...


if __name__ == "__main__":
    g = Game()
    g.start()

