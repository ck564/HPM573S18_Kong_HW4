"""
Problem 2: A Game of Chance with an Unfair Coin (Weight 1). Modify your model
for Problem 1 so that you can specify the probability that a coin flip results
in head. What is the average reward when this probability is 0.4?
"""

import HW4_P1 as G

TOSSES = 20
PROBABILITY = 0.4
GAMES = 1000

# Create game
myRepeatedGame = G.RepeatedGame(id=1, prob=PROBABILITY, iterations=GAMES)

# Simulate game
myRepeatedGame.simulate(n_times=TOSSES)

# Print the expected value of game
print("Expected value of game: $", myRepeatedGame.get_expected_value())


