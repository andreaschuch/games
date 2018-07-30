# About this project
The goal of this project is to implement games (such as [TicTacToe](https://en.wikipedia.org/wiki/Tic-tac-toe)) in python with a focus on the following functionalities:
1. GUI-based interaction allowing users to play the game
2. automization of players allowing users to play against a machine player 
3. training and evaluation of machine-learning-based players.

For more details regarding the current state, please setup project and [generate the doxygen documentation](#how-to-generate-the-documentation)

# How to setup this project
1. git clone https://github.com/andreaschuch/games
2. Install python, see https://wiki.python.org/moin/BeginnersGuide/Download
3. Install  matplotlib: https://matplotlib.org/users/installing.html#installing
4. Install doxygen: http://www.doxygen.nl/install.html

# How to run this project
python Experiment.py

# How to run the unittests
python -m unittest tests/<TestFile.py>

# How to generate the documentation
1. doxygen Doxyfile
2. Open file index.html in folder html.

# TODO's
Here is the current list of features I would like to add:
- Store trained learners in a database.
- More intuitiv unified GUI for training as well as manual and automated testing.
- Other games, e.g. [Connect 4](https://en.wikipedia.org/wiki/Connect_Four).
- Improve RL.
