# A builder is looking to build a row of N houses that can be of K different
# colors. He has a goal of minimizing cost while ensuring that no two
# neighboring houses are of the same color.

# Given an N by K matrix where the nth row and kth column represents the cost
# to build the nth house with kth color, return the minimum cost which achieves
# this goal.

def min_cost(house_costs, i, prev):
    if i >= len(house_costs): return 0

    if len(house_costs[0]) < 2: return -1

    house = house_costs[i]
    if len(house_costs[0]) == 2:
        cur = prev + 1 % 2
        return house[cur] + min_cost(house_costs, i + 1, cur)

    n = len(house_costs[0])
    mins = [prev + 1 % n, prev + 2 % n]
    if house[mins[0]] > house[mins[1]]:
        mins = [mins[1], mins[0]]

    for k in range(n):
        if k == prev: continue
        if house[k] < mins[1]:
            mins[1] = k
        if mins[0] > mins[1]:
            mins = [mins[1], mins[0]]

    cost0 = house[mins[0]] + min_cost(house_costs, i + 1, mins[0])
    cost1 = house[mins[1]] + min_cost(house_costs, i + 1, mins[1])

    return min(cost0, cost1)
