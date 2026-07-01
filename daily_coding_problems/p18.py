# Given an array of integers and a number k, where 1 <= k <= length of the
# array, compute the maximum values of each subarray of length k.

# For example, given array = [10, 5, 2, 7, 8, 7] and k = 3, we should get: [10,
# 7, 8, 8], since:

# 10 = max(10, 5, 2)
# 7 = max(5, 2, 7)
# 8 = max(2, 7, 8)
# 8 = max(7, 8, 7)
# Do this in O(n) time and O(k) space. You can modify the input array in-place
# and you do not need to store the results. You can simply print them out as
# you compute them.

from collections import deque

def sliding_max(nums, k):
    maxes = deque()

    output = []
    for i in range(len(nums)):
        maxes.append(i)

        if maxes[0] == i - k: maxes.popleft()
        while nums[maxes[-1]] > nums[maxes[0]]:
            maxes.popleft()

        if i >= k - 1:
            output.append(nums[maxes[0]])

    return output

print(sliding_max([10, 5, 2, 7, 8, 7], 3))

