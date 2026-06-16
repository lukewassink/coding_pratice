def brute_force(nums):
    prods = []
    for i, _ in enumerate(nums):
        prod = 1
        for j, _ in enumerate(nums):
            if j != i:
                prod *= nums[j]
        prods.append(prod)
    return prods


def division(nums):
    prod = 1
    zero_ind  = -1
    for i, num in enumerate(nums):
        if num == 0:
            if zero_ind != -1:
                return [0] * len(nums)
            zero_ind = i
        else:
            prod *= num

    if zero_ind != -1:
        return [0] * zero_ind + [prod] + [0] * (len(nums) - 1 - zero_ind)

    prods = []
    for num in nums:
        prods.append(prod // num)
    return prods


test_cases = [
        [1, 2, 3],
        [2,2,2],
        [0,1,2],
        [0,0,1],
        [2,2,5,3]
        ]

for case in test_cases:
    print("Case: " + str(case))
    print(brute_force(case))
    print(division(case))

