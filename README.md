# Artificial Intelligence Nanodegree
## Introductory Project: Diagonal Sudoku Solver

# Question 1 (Naked Twins)
Q: How do we use constraint propagation to solve the naked twins problem?  
A: If we have two boxes in a single unit that are the same (they are both '23' for example) the 
constraints of sudoku tell us that one of those two boxes has to be 2 and
the other has to be 3. Therefore we can eliminate 2 and 3 from the 
possibilities for the other boxes in the unit. The reduced possibilities for the
boxes in this unit impose further constraints on the possibilities for boxes in other units 
so the constraints 'propagate' through the board.

# Question 2 (Diagonal Sudoku)
Q: How do we use constraint propagation to solve the diagonal sudoku problem?  
A: To solve the diagonal sudoko problem we can use the exact same techniques as
regular sudoku. The only adjustment we have to make is adding the two diagonal as
units to our unitlist. By adding the diagonals as units we are imposing additional
constraints on the board and so constraint propagation will be even more effective than
regular sudoku.

### Install

This project requires **Python 3**.

We recommend students install [Anaconda](https://www.continuum.io/downloads), a pre-packaged Python distribution that contains all of the necessary libraries and software for this project. 
Please try using the environment we provided in the Anaconda lesson of the Nanodegree.

##### Optional: Pygame

Optionally, you can also install pygame if you want to see your visualization. If you've followed our instructions for setting up our conda environment, you should be all set.

If not, please see how to download pygame [here](http://www.pygame.org/download.shtml).

### Code

* `solutions.py` - You'll fill this in as part of your solution.
* `solution_test.py` - Do not modify this. You can test your solution by running `python solution_test.py`.
* `PySudoku.py` - Do not modify this. This is code for visualizing your solution.
* `visualize.py` - Do not modify this. This is code for visualizing your solution.

### Visualizing

To visualize your solution, please only assign values to the values_dict using the ```assign_values``` function provided in solution.py

### Data

The data consists of a text file of diagonal sudokus for you to solve.
