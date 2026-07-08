# Implement locking in a binary tree. A binary tree node can be locked or
# unlocked only if all of its descendants or ancestors are not locked.

# Design a binary tree node class with the following methods:

# - is_locked, which returns whether the node is locked
# - lock, which attempts to lock the node.  If it cannot be locked, then it
#   should return false.  Otherwise, it should lock it and return true.
# - unlock, which unlocks the node. If it cannot be unlocked, then it should
#   return false. Otherwise, it should unlock it and return true.
#
# You may augment the node to add parent pointers or any other
# property you would like. You may assume the class is used in
# a single-threaded program, so there is no need for actual locks or mutexes.
# Each method should run in O(h), where h is the height of the tree.


class Node:
    def __init__(self, _val, _left = None, _right = None):
        self.val = _val
        self.parent = None
        self.left = _left
        if self.left:
            self.left.parent = self
        self.right = _right
        if self.right:
            self.right.parent = self

        self.lockedDescendants = 0
        self.locked = False

    def ancestorLocked(self):
        parent = self.parent
        while parent:
            if parent.locked: return True
            parent = parent.parent
        return False

    def lock(self):
        if self.lockedDescendants > 0: return False
        if self.locked: return False
        if self.ancestorLocked(): return False

        self.locked = True
        parent = self.parent
        while parent:
            parent.lockedDescendants += 1
            parent = parent.parent
        return True

    def unlock(self):
        if not self.locked: return False

        parent = self.parent
        while parent:
            parent.lockedDescendants -= 1
            parent = parent.parent
        self.locked = False
        return True


tree = Node(1, Node(2), Node(3, Node(4)))
print(tree.lock() == True)
print(tree.lock() == False)
print(tree.left.lock() == False)
print(tree.left.unlock() == False)
print(tree.unlock() == True)
print(tree.right.lock() == True)
print(tree.lock() == False)
print(tree.right.left.lock() == False)
print(tree.right.unlock() == True)
print(tree.right.left.lock() == True)
