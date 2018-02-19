import HW4_P1 as G

TOSSES = 20
PROBABILITY = 0.5
GAMES = 1000

# Create game
myRepeatedGame = G.RepeatedGame(id=1, prob=PROBABILITY, iterations=GAMES)

# Simulate game
myRepeatedGame.simulate(n_times=TOSSES)

# Print the expected value of game
print("Expected value of game: $", myRepeatedGame.get_expected_value())
