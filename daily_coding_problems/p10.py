# Implement a job scheduler which takes in a function f and an integer n, and
# calls f after n milliseconds.

import time

def schedule(f, n):
    time.sleep(n/1000)
    f()

def say_hi():
    print("Hi there!")

schedule(say_hi, 2000)
