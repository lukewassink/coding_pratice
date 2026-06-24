# Implement an autocomplete system. That is, given a query string s and a set of
# all possible query strings, return all strings in the set that have s as
# a prefix.

# For example, given the query string de and the set of strings [dog, deer,
# deal], return [deer, deal].

class Node:
    def __get_words(self, pref):
        words = []
        if self.is_word:
            words.append(pref)
        for c, n in self.kids.items():
            words += n.__get_words(pref + c)
        return words

    def __init__(self):
        self.is_word = False
        self.kids = {}

    def insert(self, word):
        if not word:
            self.is_word = True
            return

        c = word[0]
        if c not in self.kids:
            self.kids[c] = Node()
        self.kids[c].insert(word[1:])

    def words_with_pref(self, pref, i = 0):
        if i < len(pref):
            if pref[i] not in self.kids:
                return []
            return self.kids[pref[i]].words_with_pref(pref, i + 1)
        
        return self.__get_words(pref)

empty_trie = Node()
print(empty_trie.words_with_pref("a"))
trie = Node()
trie.insert("dog")
trie.insert("deer")
trie.insert("deal")
print(trie.words_with_pref("de"))
print(trie.words_with_pref("z"))
print(trie.words_with_pref("deers"))
print(trie.words_with_pref(""))
