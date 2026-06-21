# A unival tree (which stands for "universal value") is a tree where all nodes
# under it have the same value. (Note: a subtree means a node and all its
# descentants.)

# Given the root to a binary tree, count the number of unival subtrees.

# For example, the following tree has 5 unival subtrees:

#    0
#   / \
#  1   0
#     / \
#    1   0
#   / \
#  1   1

class Node:
    def __init__(self, val=0, kids=[]):
        self.val = val
        self.kids = kids

def count_univals_helper(node):
    count = 0
    val = node.val
    for kid in node.kids:
        c, v = count_univals_helper(kid)
        if v != val:
            val = -1
        count += c

    return count + (val != -1), val

def count_univals(node):
    return count_univals_helper(node)[0]


tree1 = Node(0)
print(count_univals(tree1))
tree2 = Node(0, [Node(1), Node(0, [Node(1, [Node(1), Node(1)]), Node(0)])])
print(count_univals(tree2))
