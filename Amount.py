"""
Leslie Horace
Amount.py: Uses backtracking to find the subsequence of unique sum combinations
Input: nums = [11, 1, 3, 2, 6, 1, 5], an array of numbers
Output: result = [[3, 5], [2, 6], [1, 2, 5], [1, 1, 6]], array of unique sum combinations
"""


def find_combinations(nums, begin, res, sum, comb):
    if sum == 0:
        # if target sum is found
        if comb not in res:
            # append to result if unique
            res.append(list(comb))
    if sum > 0:
        # if target sum is not found, loop to find the next target com
        for x in range(begin, len(nums)):
            # append the next num
            comb.append(nums[x])
            # recurse to permute the next comb, hence begin = x+1
            find_combinations(nums, x+1, res, sum - nums[x], comb)
            # remove last num in comb to backtrack, prepping for next comb
            comb.pop()
    # here if all unique comb are found
    return res[::-1]


def amount(A, S):
    A.sort() # sort input nums to ensure all combs are unique
    return find_combinations(A, 0, [], S, [])
