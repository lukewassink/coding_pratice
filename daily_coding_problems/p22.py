# Given a dictionary of words and a string made up of those words (no spaces),
# return the original sentence in a list. If there is more than one possible
# reconstruction, return any of them. If there is no possible reconstruction,
# then return null.

# For example, given the set of words 'quick', 'brown', 'the', 'fox', and the
# string "thequickbrownfox", you should return:

# ['the', 'quick', 'brown', 'fox'].

# Given the set of words 'bed', 'bath', 'bedbath', 'and', 'beyond', and the
# string "bedbathandbeyond", return either ['bed', 'bath', 'and', 'beyond] or
# ['bedbath', 'and', 'beyond'].

class Trie:
    def __init__(self):
        self._kids = [None] * 26
        self._isWord = False

    def insert(self, word, i = 0):
        if i == len(word):
            self._isWord = True
            return
        idx = ord(word[i]) - ord('a')
        if not self._kids[idx]:
            self._kids[idx] = Trie()
        self._kids[idx].insert(word, i + 1)

    def insertWords(self, *args):
        for word in args:
            self.insert(word)

    def hasPrefix(self, pref, i = 0, requireWord = False):
        if i == len(pref):
            return self._isWord or not requireWord
        
        idx = ord(pref[i]) - ord('a')
        if not self._kids[idx]:
            return False
        return self._kids[idx].hasPrefix(pref, i + 1, requireWord)

    def hasWord(self, word):
        return self.hasPrefix(word, 0, True)

    def sentences(self, s, i = 0, j = 0):
        w = s[i:j]
        if j == len(s):
            return [[w]]

        if not self.hasPrefix(w):
            return []

        sentences = self.sentences(s, i, j + 1)

        if self.hasWord(w):
            withWord = self.sentences(s, j, j + 1)
            for sentence in withWord:
                sentence.insert(0, w)
            sentences += withWord

        return sentences


t = Trie()
t.insertWords('quick', 'brown', 'the', 'fox')
print(t.sentences("thequickbrownfox"))

t2 = Trie()
t2.insertWords('bed', 'bath', 'bedbath', 'and', 'beyond')
print(t2.sentences("bedbathandbeyond"))

