# Given two singly linked lists that intersect at some point, find the
# intersecting node. The lists are non-cyclical.

# For example, given A = 3 -> 7 -> 8 -> 10 and B = 99 -> 1 -> 8 -> 10, return
# the node with value 8.

# In this example, assume nodes with the same value are the exact same node
# objects.

# Do this in O(M + N) time (where M and N are the lengths of the lists) and
# constant space.

class Node:
    def __init__(self, _val, _next=None):
        self.val = _val
        self.next = _next
        self._length = -1

    def length(self):
        if self._length > 0:
            return self._length
        if not self.next:
            self._length = 1
        else:
            self._length = 1 + self.next.length()
        return self._length

# Faster but more memory.
def intersectingNode_1(a, b):
    aNodes = set()
    while a:
        aNodes.add(a)
        a = a.next
    while b:
        if b in aNodes:
            return b
        b = b.next

    return None

# Slightly slower, but constant memory
def intersectingNode_2(a, b):
    if b.length() > a.length():
        t = a
        a = b
        b = t

    for _ in range(a.length() - b.length()):
        a = a.next

    while a != b:
        a = a.next
        b = b.next

    return a

x = Node(3, Node(4, Node(5)))
a = Node(1, Node(2, x))
b = Node(11, x)

print(intersectingNode_1(a, b).val)
print(intersectingNode_2(a, b).val)
