import random

def sample(stream):
    if not stream.hasNext():
        raise IndexError("Cannot sample an empty stream.")

    el = stream.next()
    i = 1
    while stream.hasNext():
        nextEl = stream.next()
        i += 1
        if random.randint(1, i) == 1:
            el = nextEl
    return el

class Stream:
    def __init__(self, _data):
        self._data = _data
        self._i = 0

    def hasNext(self):
        return self._i < len(self._data)

    def next(self):
        el = self._data[self._i]
        self._i += 1
        return el


freq = [0] * 7
for _ in range(1000):
    stream = Stream([0, 1, 2, 3, 4, 5, 6])
    el = sample(stream)
    freq[el] += 1

print(freq)
