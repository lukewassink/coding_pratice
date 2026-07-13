# Write an algorithm to justify text. Given a sequence of words and an integer
# line length k, return a list of strings which represents each line, fully
# justified.

# More specifically, you should have as many words as possible in each line.
# There should be at least one space between each word. Pad extra spaces when
# necessary so that each line has exactly length k. Spaces should be
# distributed as equally as possible, with the extra spaces, if any,
# distributed starting from the left.

# If you can only fit one word on a line, then you should pad the right-hand
# side with spaces.

# Each word is guaranteed not to be longer than k.

# For example, given the list of words ["the", "quick", "brown", "fox",
# "jumps", "over", "the", "lazy", "dog"] and k = 16, you should return the
# following:

# ["the  quick brown", # 1 extra space on the left
# "fox  jumps  over", # 2 extra spaces distributed evenly
# "the   lazy   dog"] # 4 extra spaces distributed evenly


def justify(text, k):
    if not text:
        return []

    output = []
    start = 0
    totalWordLength = 0

    for i, w in enumerate(text):
        totalWordLength += len(w)
        lenWithNextWord = totalWordLength + i - start
        if i + 1 < len(text):
            lenWithNextWord += len(text[i + 1]) + 1

        if lenWithNextWord > k or i == len(text) - 1:
            output += [text[start]]
            
            if i == start:
                output[-1] += " " * (k - len(w))
            else:
                spaces = (k - totalWordLength) // (i - start)
                extraSpaces = (k - totalWordLength) % (i - start)

                for j in range(i - start):
                    whiteSpace = " " * (spaces + 1 if j < extraSpaces else spaces)
                    output[-1] += whiteSpace + text[start + j + 1]

            start = i + 1
            totalWordLength = 0

    return output

def printList(l):
    print()
    for word in l:
        print(word)

text = ["the", "quick", "brown", "fox", "jumps", "over", "the", "lazy", "dog"]
printList(justify(text, 16))

text2 = ["the", "quick", "brown", "blerghhhhhhhh", "fox", "jumps", "over",
         "the", "lazy", "dog", "toodles"]
printList(justify(text2, 16))
