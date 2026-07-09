# Implement regular expression matching with the following special characters:

# . (period) which matches any single character
# * (asterisk) which matches zero or more of the preceding element
# That is, implement a function that takes in a string and a valid regular
# expression and returns whether or not the string matches the regular
# expression.

# For example, given the regular expression "ra." and the string "ray", your
# function should return true. The same regular expression on the string
# "raymond" should return false.

# Given the regular expression ".*at" and the string "chat", your function
# should return true. The same regular expression on the string "chats" should
# return false.

def matches(p, s):
    m = len(p)
    n = len(s)
    cache = [-1] * m * n

    def at(i, j):
        # i in p, j in s
        return cache[i * m + j]

    def set(i, j, val):
        cache[i * m + j] = val

    def dpMatches(i = 0, j = 0):
        if j == n or i == m:
            return j == n and i == m

        if at(i, j) >= 0:
            return at(i, j) == 1

        if p[i] == '.':
            return dpMatches(i + 1, j + 1)

        if p[i] == '*':
            return dpMatches(i, j + 1) or dpMatches(i + 1, j + 1)

        set(i, j, p[i] == s[j] and dpMatches(i + 1, j + 1))
        return at(i, j)

    return dpMatches()

print(matches("ra.", "ray") == True)
print(matches("ra.", "rayond") == False)
print(matches(".*at", "chat") == True)
print(matches(".*at", "Chats") == False)
