from TicTacToe import TicTacToe
from Learner import Learner
from Players import RandomPlayer
from Players import HumanPlayer
from Players import PlayerTypes
from Players import DeterministicPlayer
import matplotlib.pyplot as plt
from Match import Match
import Gui
import argparse


##
# Trains a learning machine player against another machine player and then tests the learners performance
# 1. against the other machine player
# 2. against a human player.
# @author Andrea Schuch
class Experiment:
    ##
    # Constructs a new experiment allowing to
    # 1. Train a machine learning-based computer player.
    # 2. Evaluating the learner's performance in automated tests against another machine player.
    # 3. Manually evaluating the performance by playing against it.
    # @param learner The machine-learning-based player to be trained and tested.
    # @param gui The Gui class to be used during manual evalutation.
    def __init__(self, learner, gui):
        self.learner = learner
        self.gui = gui
        self.reinit()

    ##
    # Re-initializes the experiment's counters.
    # Should be called after each run() for training or testing.
    def reinit(self):
        self.matches = 0
        self.won = 0
        self.wonplot = []
        self.lost = 0
        self.lostplot = []
        self.draw = 0
        self.drawplot = []

    ##
    # Trains the learner by letting it play against another player and displays the learner's performance.
    # @param trainer The other player used for training the learner.
    # @param no_of_training_rounds Number of matches to be played.
    def train(self, trainer, no_of_training_rounds=1000):
        print('----- Training:-----')
        for X in range(no_of_training_rounds):
            self.run(self.learner, trainer)
            experiment.evaluate(trainer)
        self.print_testresult()
        self.plot_trained()
        self.reinit()

    ##
    # Displays how the learner performed during the training.
    def plot_trained(self):
        fig, ax = plt.subplots()
        ax.plot(range(self.matches), experiment.wonplot, label='won')
        ax.plot(range(self.matches), experiment.lostplot, label='lost')
        ax.plot(range(self.matches), experiment.drawplot, label='draw')

        ax.set(xlabel='number of games')
        ax.set(ylabel='percentage of games')
        ax.set(title='Learner Performance')
        plt.legend()
        plt.show(block=False)

    ##
    # Tests the learner by letting it play against another player.
    # @param tester The other player used for testing the learner.
    # @param no_of_testrounds Number of matches to be played. Defaults to 100.
    def test(self, other_player, no_of_testrounds=None):
        if not no_of_testrounds:
            no_of_testrounds=100
        if (other_player.type==PlayerTypes.HUMAN):
            print('----- Manual Testing:-----')
        elif(other_player.type==PlayerTypes.MACHINE):
            print('----- Automated Testing:-----')
        for X in range(no_of_testrounds):
            self.run(self.learner, other_player)

        self.print_testresult()
        self.reinit()

    ##
    # Displays how the learner performed during the test.
    def print_testresult(self):
        print('won=' + str(experiment.won))
        print('lost=' + str(experiment.lost))
        print('draw=' + str(experiment.draw))

    ##
    # Runs a match and stores the result.
    def run(self, player, other_player):
        self.game = TicTacToe()
        gui = None
        if other_player.type==PlayerTypes.HUMAN:
            gui = self.gui(self.game)
        self.match = Match(gui, self.game, players=[player, other_player])
        self.match.play()


        self.matches = self.matches + 1
        #print('\n')
        if self.match.winner == self.learner:
            self.won += 1
            #print('won')
        elif self.match.winner == other_player:
            self.lost += 1
            #print('lost')
        else:
            self.draw += 1
            #print('draw')
        self.wonplot.append(self.won/self.matches)
        self.drawplot.append(self.draw/self.matches)
        self.lostplot.append(self.lost/self.matches)

    # Evaluates the outcome of a match for the learner to learn.
    # @param  other_player The other player.
    def evaluate(self, other_player):
        if self.match.winner == self.learner:
            reward = 100
        elif self.match.winner == other_player:
            reward = -100
        else:
            reward = -50
        self.learner.learn(self.game, reward, self.match.current_player())


if __name__ == '__main__':
    learner = Learner('X')
    other_mark = 'O'
    experiment = Experiment(learner, Gui.KtinterGui)

    trainer = RandomPlayer(other_mark)
    tester1 = RandomPlayer(other_mark)
    tester2 = HumanPlayer(other_mark)

    parser = argparse.ArgumentParser(description='Configures the experiment.')
    parser.add_argument('-train','--no_of_training_rounds', type=int, default=1000,
                        help='Number of training rounds')
    parser.add_argument('-atest','--number_of_automated_testrounds', type=int, default=100,
                        help='Number of testing rounds for automated evaluation')
    parser.add_argument('-mtest','--number_of_manual_testrounds', type=int, default=1,
                        help='Number of testing rounds for manual evaluation')
    parser.add_argument('-prewards','--print_reward_table', type=bool, default=False,
                        help='Prints out the internal reward table of the learner after training.')
    args = parser.parse_args()

    experiment.learner.random_exploration = False
    experiment.train(trainer, args.no_of_training_rounds)

    if (args.print_reward_table):
        print('----- Reward Values:-----')
        print(learner.rewards)

    learner.random_exploration = False
    experiment.test(trainer, args.number_of_automated_testrounds)

    experiment.test(tester2, args.number_of_manual_testrounds)

