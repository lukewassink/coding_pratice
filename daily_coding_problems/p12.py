# There exists a staircase with N steps, and you can climb up either 1 or
# 2 steps at a time. Given N, write a function that returns the number of
# unique ways you can climb the staircase. The order of the steps matters.

# For example, if N is 4, then there are 5 unique ways:

# 1, 1, 1, 1
# 2, 1, 1
# 1, 2, 1
# 1, 1, 2
# 2, 2
# What if, instead of being able to climb 1 or 2 steps at a time, you could
# climb any number from a set of positive integers X? For example, if X = {1,
# 3, 5}, you could climb 1, 3, or 5 steps at a time.

from functools import reduce

# We can climb 1 or 2 steps.
def num(n):
    match n:
        case 0:
            return 1
        case 1:
            return 1
        case 2:
            return 2

    return num(n - 1) + num(n - 2)

print(num(0))
print(num(1))
print(num(2))
print(num(3))
print(num(4))


# We can climb any number of steps in X.
# This is really nice! This code is making me happy!
def num_x(n, X):
    if n < 0: return 0
    if n == 0: return 1

    return reduce(lambda x, y: x + num_x(n - y, X), X, 0)

print("X version:")
print(num_x(10, []))
print(num_x(1, [2]))
print(num_x(4, [1, 2]))
print(num_x(3, [1, 2, 3]))
print(num_x(3, [2, 3]))

