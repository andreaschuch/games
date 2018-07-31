from tkinter import *
from TicTacToe import TicTacToe
from abc import ABC, abstractmethod
from Players import Player
import os

# @author Andrea Schuch


##
# Provides interface that allows a human player to play a game.
# Note: This is an abstract interface that cannot be instantiated, please instantiate one of the subclasses.
class Gui(ABC):
    ##
    # Constructs a gui application for a given game.
    # @param The game.
    @abstractmethod
    def __init__(self, game):
        pass
    ##
    # Starts the game. Should be called at the beginning of the game.
    @abstractmethod
    def start(self):
        pass

    ##
    # Retrieves the human player's next move, at the current state of the game, by asking the user.
    # @param game The game.
    # @return The move chosen by the player.
    @abstractmethod
    def next_move(self):
        pass


    ##
    # Ends the game. Should be called when the game is over.
    @abstractmethod
    def game_over(self):
        pass

##
# Provides a graphical interface that allows a human player to play a game.
# @author Andrea Schuch
class KtinterGui(Gui):
    # todo: game title
    # todo: which player

    def __init__(self, game):
        self.game = game
        self.root = Tk()
        self.user_input = False
        self.buttons = [[None for i in range(self.game.board_size())] for j in range(self.game.board_size())]
        for row in range(self.game.board_size()):
            for column in range(self.game.board_size()):
                button = Button(self.root)
                button.configure(text='  ', command=lambda row=row, column=column: self.play_command(row, column, self.current_player))
                button.grid(row=row, column=column)
                self.buttons[row][column] = button

    def play_command(self, row, column, player):
        button = self.buttons[row][column]
        success = self.game.play(row=row, column=column, player=player)
        if success:
            self.user_input = (row, column)
            self.play_view(row, column, player)
        return success

    def play_view(self, row, column, player):
        button = self.buttons[row][column]
        button.configure(text=player.name, state=DISABLED)
        is_winner = self.game.is_winner(player)
        if is_winner:
            for field in is_winner:
                button = self.buttons[field[0]][field[1]]
                button.configure(bg='red')
        self.root.update()

    def start(self):
         self.root.update()

    def next_move(self, player):
        self.user_input = None
        self.current_player = player
        while(not self.user_input):
            self.root.update()
        user_input = self.user_input
        self.user_input = None
        return user_input

    def game_over(self, winner=None):
        for row in range(self.game.board_size()):
            for column in range(self.game.board_size()):
                self.buttons[row][column].configure(state=DISABLED)
        self.root.update()
        self.root.mainloop()


##
# Provides a command line based interface that allows a human player to play a game.
# @author Andrea Schuch
class CommandlineGui(Gui):

    def __init__(self, game):
        self.game = game

    def start(self):
        os.system('cls')
        self.game.print_board()

    def play_view(self, row, column, player):
        os.system('cls')
        self.game.print_board()

    def next_move(self, player):
        print("Player {}, your turn :-)".format(player.name))
        while True:
            try:
                row = int(input("Which row?"))
                if row >  self.game.board_size() or row < 1:
                    raise IndexError
                break
            except IndexError:
                print('This board has {board_size} columns. Please provide a number between 1 and {board_size}.'.format(board_size=self.game.board_size()))
            except ValueError:
                print('Please provide a number between 1 and {} without extra characters.'.format(self.game.board_size()))
        while True:
            try:
                column = int(input("Which column in row {}?".format(row)))
                if column >  self.game.board_size() or column < 1:
                    raise IndexError
                break
            except IndexError:
                print('Row {row} has {board_size} columns. Please provide a number between 1 and {board_size}.'.format(row=row, board_size=format(self.game.board_size())))
            except ValueError:
                print('Please provide a number between 1 and {} without extra characters.'.format(self.game.board_size()))
        move = (row-1, column -1)
        played = self.game.play(*move, player)
        self.play_view(*move, player)
        if played:
            return move
        else:
            print('Try again!')
            return None

    def play_command(self, row, column, player):
        success = self.game.play(row=row, column=column, player=player)
        os.system('cls')
        self.game.print_board()
        return success

    def game_over(self, winner=None):
            if winner:
                print ("Congratulations {}!".format(winner.name))
            else:
                print("It's a draw!")

if __name__ == '__main__':
    game = TicTacToe()
    player = Player()
    gui = KtinterGui(game)
    gui.start()
    move1 = (1,1)
    gui.game.play(*move1, player)
    gui.play_view(*move1, player)

    move2 = gui.next_move(player)
    gui.play_view(*move2, player)

    gui.game_over()
    gui.game_over(player)