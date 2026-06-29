# You run an e-commerce website and want to record the last N order ids in
# a log. Implement a data structure to accomplish this, with the following API:

# -- record(order_id): adds the order_id to the log
# -- get_last(i): gets the ith last element from the log. i is guaranteed to be
#    smaller than or equal to N.

# You should be as efficient with time and space as possible.

# Assumptions:
# 1) "ith last" means ith most recent
# 2) the log can fit in memory

class Node:
    def __init__(self, _val, _next_node = None):
        self.val = _val
        self.next_node = _next_node
        self.prev_node = None

class Log:

    def __init__(self, _max_size):
        self.max_size = _max_size
        self.begin = None
        self.end = None
        self.offset = 0
        self.index_to_node = {}

    def record(self, order_id):
        order_node = Node(order_id, self.begin)
        if self.begin:
            self.begin.prev_node = order_node
            self.begin = order_node
        else:
            self.begin = order_node
            self.end = order_node

        self.index_to_node[self.offset] = self.begin
        self.offset += 1

        size = len(self.index_to_node)
        if size > self.max_size:
            self.end = self.end.prev_node
            self.end.next_node = None
            del self.index_to_node[self.offset - size]

    def get_last(self, i):
        if (i > len(self.index_to_node)):
            raise IndexError("There are fewer than " + str(i)\
                    + " elements in the log")
        return self.index_to_node[self.offset - i].val

log = Log(3)
log.record(1)
log.record(2)
log.record(3)
log.record(4)
log.record(5)
log.record(6)

print(log.get_last(1))
print(log.get_last(2))
print(log.get_last(3))
# print(log.get_last(4))

