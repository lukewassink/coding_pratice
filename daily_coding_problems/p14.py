# The area of a circle is defined as πr^2. Estimate π to 3 decimal places using
# a Monte Carlo method.

# Note: with 1,000,000 rounds it estimated pi = 3.142964, so it converges quite
# slowly.

import random

def monte_carlo_pi(rounds):
    circle_hits = 0
    for _ in range(rounds):
        x = random.uniform(0, 1)
        y = random.uniform(0, 1)
        if (x*x + y*y) <= 1: circle_hits += 1

    return 4 * circle_hits / rounds


print(monte_carlo_pi(1000000))
