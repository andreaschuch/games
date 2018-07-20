from TicTacToe import TicTacToe
from Learner import Learner
from Players import RandomPlayer
from Players import HumanPlayer
from Players  import PlayerTypes
import matplotlib.pyplot as plt
from Match import Match
from Gui import CommandlineGui
from Gui import KtinterGui


##
# This class trains a learning machine player against another machine player and then tests the learners performance
# 1. against the other machine player
# 2. against a human player.
# @author Andrea Schuch
class Experiment:

    def __init__(self, no_of_training_rounds, learner, gui):
        self.no_of_training_rounds = no_of_training_rounds
        self.learner = learner
        self.won = 0
        self.wonplot = []
        self.lost = 0
        self.lostplot = []
        self.draw = 0
        self.drawplot = []
        self.matches = 0
        self.gui=gui

    def train(self, trainer):
        print('----- Training:-----')
        for X in range(experiment.no_of_training_rounds):
            self.run(self.learner, trainer)
            experiment.evaluate(trainer)

    def test(self, other_player, no_of_testrounds):
        if (other_player.type==PlayerTypes.HUMAN):
            print('----- Manual Testing:-----')
        elif(other_player.type==PlayerTypes.MACHINE):
            print('----- Automated Testing:-----')
        for X in range(no_of_testrounds):
            self.run(self.learner, other_player)

    def run(self, player, other_player):
        self.game = TicTacToe()
        gui = None
        if other_player.type==PlayerTypes.HUMAN:
            gui = self.gui(self.game)
        self.match = Match(gui, self.game, players=[player, other_player])
        self.match.play()


        self.matches +=1
        if (not self.game.available_moves()):
            #print('draw')
            self.draw +=1
        elif self.game.is_winner(self.match.current_player()):
            #print ('winner=' + current_player.name)
            if self.match.current_player() == player:
                 self.won +=1
            if self.match.current_player()==other_player:
                 self.lost +=1
        self.wonplot.append(self.won/self.matches)
        self.drawplot.append(self.draw/self.matches)
        self.lostplot.append(self.lost/self.matches)

    def evaluate(self, other_player):
        if self.game.is_winner(self.learner):
            reward = 100
        elif self.game.is_winner(other_player):
            reward = -100
        else:
            reward = 0
        self.learner.learn(self.game, reward, self.match.current_player())


if __name__=='__main__':
    learner = Learner('X')
    experiment = Experiment(100000, learner, KtinterGui)

    trainer = RandomPlayer('O')
    tester1 = RandomPlayer('O')
    tester2 = HumanPlayer('O')

    learner.random_exploration=True
    experiment.train(trainer)
    print('won=' + str(experiment.won))
    print('lost=' + str(experiment.lost))
    print('draw=' + str(experiment.draw))

    experiment.won=0
    experiment.lost=0
    experiment.draw=0
    #print(experiment.learner.rewards)
    fig, ax = plt.subplots()
    ax.plot(range(experiment.no_of_training_rounds),experiment.wonplot, label='won')
    ax.plot(range(experiment.no_of_training_rounds),experiment.lostplot, label='lost')
    ax.plot(range(experiment.no_of_training_rounds),experiment.drawplot, label='draw')

    ax.set(xlabel='number of games')
    ax.set(ylabel='percentage of games')
    ax.set(title='Learner Performance')
    plt.legend()
    plt.show(block=False)

    experiment.won=0
    experiment.lost=0
    experiment.draw=0

    learner.random_exploration = False
    experiment.test(tester1, 100)
    print('won='+str(experiment.won))
    print('lost='+str(experiment.lost))
    print('draw='+str(experiment.draw))

    experiment.won=0
    experiment.lost=0
    experiment.draw=0

    experiment.test(tester2, 2)
    print('won='+str(experiment.won))
    print('lost='+str(experiment.lost))
    print('draw='+str(experiment.draw))

