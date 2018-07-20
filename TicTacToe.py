from Players import Player


##
# The game of <a href="https://en.wikipedia.org/wiki/Tic-tac-toe">TicTacToe</a>.
class TicTacToe:
    ##
    # Initializes a TicTacToe game on a quadratic board.
    # @param board_size The size of the board. For example, a board sized 3 has 9 fields.
    def __init__(self, board_size=3):
        self.board = [[None for i in range(board_size)] for j in range(board_size)]

    ##
    # Places the player's marking at the indicated field on the board, if that field has not yet been taken.
    # @param player The current player.
    # @param row Row position of the desired field.
    # @param column Column position of the desired field.
    def play(self,  row, column, player):
        if self.retrieve(row, column)is None:
            self.board[row][column] = player.name
            return True
        else:
            return False

    ##
    # Retrieves the players' markings from the board at a specified field.
    # @param row Row position of the desired field.
    # @param column Column position of the desired field.
    # @return The player's marking. Returns None if the field has not yet been taken.
    def retrieve(self, row, column):
        return self.board[row][column]

    ##
    #  Prints the board to standard output in human-readable format.
    def print_board(self):
        print('Board:')
        for row in self.board:
            print(row)
        print('\n')

    ##
    # Provides the size of the board as a convenience for looping. Note that boards are always quadratic.
    # @return the size of the board (usually 3).
    def board_size(self):
        return len(self.board);

    ##
    # Checks if a player has won the game, and returns the fields that made the victory.
    # A player has won if he has placed his marks in a line covering the board from one side to the other.
    # The line can be horizontal, vertical or diagonal.
    # Note: Will not retrieve multiple lines.
    # @return The list of winning fields that make up the line.
    def is_winner(self, player):
        fields = []

        for row in range(self.board_size()):
            winning_row = True
            for column in range(self.board_size()):
                if self.board[row][column] != player.name:
                    winning_row = False
                    break
            if winning_row:
                for column in range(self.board_size()):
                    fields.append((row, column))
                return fields

        for column in range(self.board_size()):
            winning_column = True
            for row in range(self.board_size()):
                if self.board[row][column] != player.name:
                    winning_column = False
                    break
            if winning_column:
                for row in range(self.board_size()):
                    fields.append((row, column))
                return fields

        tictactoe_diagonal1 = True
        for row in range(self.board_size()):
            if self.board[row][row]!=player.name:
                tictactoe_diagonal1 = False
                break
            else:
                fields.append((row,row))
        if tictactoe_diagonal1:
            return fields
        else:
            fields = []

        tictactoe_diagonal2 = True
        column = self.board_size()-1
        for row in range(self.board_size()):
            if self.board[row] [column] != player.name:
                tictactoe_diagonal2 = False
                fields.clear()
                break
            else:
                fields.append((row,column))
                column = column - 1

        if tictactoe_diagonal2:
            return fields
        else:
            fields = []

        return fields

    ##
    # Compiles the list of next move options given the current state of the game.
    # Players can only choose between fields that have not been taken, yet.
    # @return The list of possible moves for the current player, i.e. all free fields on the board.
    def available_moves(self):
        available_moves = [(row, column) for row in range(self.board_size()) for column in range(self.board_size()) if not self.retrieve(row, column)]
        return available_moves

if __name__=='__main__':
    tictactoe = TicTacToe(board_size=3)
    tictactoe.print_board()
    for row in range(tictactoe.board_size()):
        for column in range(tictactoe.board_size()):
            tictactoe.play(row=row,column=column,player=Player())
    tictactoe.print_board()
    for row in range(tictactoe.board_size()):
        for column in range(tictactoe.board_size()):
            print(tictactoe.retrieve(row=row,column=column))