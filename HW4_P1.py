"""
Problem 1: A Game of Chance (Weight 3).
You can enter in a game where you get to flip a fair coin 10 times, and
you will receive $100 any time you get a “Head” after two consecutive “Tail”?
If you need to pay $250 to enter in the game, estimate the expected reward
using Monte Carlo simulation.

- This experiment involves 20 random events {𝐸1,𝐸2,𝐸3,…,𝐸20}, where each event
𝐸𝑖 results in either of two outcomes {Head, Tail}.
- Whenever {Tail, Tail, Head} occurs, we receive $100
- If we use random variable 𝑋 to denote the total reward, then:

- 𝑋 =$0−$250=−$250 if {Tail, Tail, Head} never occurs
- 𝑋 =$100−$250=−$150 if {Tail, Tail, Head} occurs once
- 𝑋 =$200−$250=−$50 if {Tail, Tail, Head} occurs twice
- And so on…
- Our goal is to estimate E[𝑋].

Develop a simulation model to get 1000 realization of 𝑋. Print the average of
these realizations as an estimate for E[𝑋].
Hints: Create a class Game that has a method attribute Simulate()
that flips a coin 20 times, find the number of times that {Tail, Tail, Head}
occurs, and return the reward (as calculated above).
"""

import numpy as np


class Game:

    def __init__(self, id, prob):
        self._id = id
        self._rnd = np.random
        self._rnd.seed(self._id)
        self._prob = prob
        self._results = []
        self._arrs = []
        self._entryfee = 250
        self._reward = 100
        self._winsequence = [0,0,1]     # Winning sequence: Tails, Tails, Heads

    def simulate(self, n_times):        # simulate n tosses for each trial
        tosses=0
        while tosses < n_times:
            if self._rnd.sample() < self._prob:
                result = 1
            else:
                result = 0
            self._results.append(result)

            tosses += 1
        return self._results

    def get_outcomes(self):
        i=0
        value = -self._entryfee
        winner = self._winsequence

        for toss in self._results:          # iterate over results to create increments of three
            triplet = self._results[i:i+3]
            self._arrs.append(triplet)
            i += 1

        for i in self._arrs:    # add 100 every time winning sequence occurs
            if i == winner:
                value += self._reward
        return value


class RepeatedGame:

    def __init__(self, id, prob, iterations):
        self._trials = []   # list of n trials
        self._value = []    # list of expected values from each trial

        for trial in range(iterations):
            trial = Game(id, prob)
            self._trials.append(trial)

    def simulate(self, n_times):
        for trial in self._trials:      # simulate n trials
            trial.simulate(n_times)

            value = trial.get_outcomes()    # obtain value for each trial
            self._value.append(value)

    def get_expected_value(self):       # obtain average value over n trials
        return sum(self._value) / len(self._value)


# Test: Individual Game

# myGame = Game(1, 0.5)
# print(myGame.simulate(20))
# print(myGame.get_outcomes())


