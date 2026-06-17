CHARS_TO_ESCAPE = ['\\', 'L', 'R']

def escape_string(s):
    escaped = ""
    for c in s:
        if c in CHARS_TO_ESCAPE:
            escaped += "\\"
        escaped += c
    return escaped

def unescape_string(s):
    unescaped = ""
    i = 0

    while i < len(s):
        if s[i] == "\\":
            i += 1
        unescaped += s[i]
        i += 1
    return unescaped

class Node:
    def __init__(self, val, left, right):
        self.val = val
        self.left = left
        self.right = right

def serialize(node, level = 0):
    s =  escape_string(str(node.val))
    if node.left != None:
        s += "L" + str(level) + "L" + serialize(node.left, level + 1)
    if node.right != None:
        s += "R" + str(level) + "R" + serialize(node.right, level + 1)
    return s

def deserialize(s, level = 0, i = 0):
    val = ""
    lnode = None
    rnode = None
    j = i
    while (j < len(s)):

        # print("char: " + s[j] + ", level: " + str(level))

        if s[j] == "\\":
            j += 1
            val += s[j]
        elif s[j] == "L":
            k = 1
            while s[k+j] != "L":
                k += 1
            n_level = int(s[j+1:j+k])
            if n_level < level:
                break
            lnode, j = deserialize(s, n_level + 1, j + k + 1) 
        elif s[j] == "R":
            k = 1
            while s[k+j] != "R":
                k += 1
            n_level = int(s[j+1:j+k])
            if n_level < level:
                break
            rnode, j = deserialize(s, n_level + 1, j + k + 1) 
        else:
            val += s[j]
            j += 1
    return Node(val, lnode, rnode), j

n = Node("root", Node("left", Node("left.left", None, None), None),
         Node("right", None, None))
print(serialize(n))
m, _ = deserialize(serialize(n))
print("Root: " + m.val)
print("Left: " + m.left.val)
print("LeftLeft: " + m.left.left.val)
print("Right: " + m.right.val)

