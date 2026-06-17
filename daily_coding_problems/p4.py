# Given an array of integers, find the first missing positive integer in linear
# time and constant space. In other words, find the lowest positive integer
# that does not exist in the array. The array can contain duplicates and
# negative numbers as well.

# Ex. [3, 4, -1, 1] -> 2
# Ex. [1, 2, 0] -> 3


def first_missing(nums):
    n = len(nums)
    
    for i, num in enumerate(nums):
        to_place = num
        displaced = 0
        nums[i] = 0

        while to_place != nums[to_place - 1]:
            if to_place > n or to_place <= 0:
                break
            displaced = nums[to_place - 1]
            nums[to_place - 1] = to_place
            to_place = displaced
        
    for i, num in enumerate(nums):
        if num == 0:
            return i + 1
    return n

print (first_missing([3, 4, -1, 1]))
print (first_missing([1, 2, 0]))
print (first_missing([1, 3, 0, 0, -5, 2, 6, 7, 7, 0, -2, 5, 1]))

