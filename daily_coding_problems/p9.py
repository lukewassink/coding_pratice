def largest_non_consecutive_sum(nums):
    cur_max = 0
    prev_max = 0

    for num in nums:
        temp = max(cur_max, prev_max, prev_max + num)
        prev_max = cur_max
        cur_max = temp

    return max(cur_max, prev_max)

print(largest_non_consecutive_sum([]))
print(largest_non_consecutive_sum([2]))
print(largest_non_consecutive_sum([2, 4, 6, 2, 5]))
print(largest_non_consecutive_sum([5, 1, 1, 5]))
print(largest_non_consecutive_sum([2, 4, 7, 3]))
print(largest_non_consecutive_sum([5, 3, -2]))
print(largest_non_consecutive_sum([0, -5, -3, -3, -5, 5, 4, -1, 3, 3]))
