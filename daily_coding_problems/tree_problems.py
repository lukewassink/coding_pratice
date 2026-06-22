class Node:
    def __init__(self, left=None, right=None, val = ""):
        self.left = left
        self.right = right
        self.val = val

def count(node):
    if not node:
        return 0
    return count(node.left) + count(node.right) + 1

def max_depth(node):
    if not node:
        return 0
    return 1 + max(max_depth(node.left), max_depth(node.right))

print(max_depth(None))
print(max_depth(Node()))
print(max_depth(Node(Node())))
print(max_depth(Node(Node(), Node())))
print(max_depth(Node(Node(Node()), Node())))
print(max_depth(Node(Node(None, Node()), Node())))
print(max_depth(Node(Node(None, Node()), Node(Node(), Node()))))

def deepest_node_helper(node):
    if not node: return node, 0
    if not node.left and not node.right: return node, 1

    lnode, ldepth = deepest_node_helper(node.left)
    rnode, rdepth = deepest_node_helper(node.right)
    if ldepth > rdepth: return lnode, ldepth + 1
    else: return rnode, rdepth + 1

def deepest_node(node):
    return deepest_node_helper(node)[0]

print(deepest_node(Node(None, None, "test")).val)
print(deepest_node(Node(Node(), Node(Node(None, None, "test")))).val)
