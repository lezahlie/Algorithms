"""
Leslie Horace
MaxSet.py:  Uses dynamic programming (Bottom up) and backtracking to find
            the maximum independent set for sums of non-adjacent numbers
Input: nums = [7,2,-4,5,8,6], an array of integers
Output: result = [7, 5, 8], an array for the max independent set
"""

def find_max_set(nums, n, sums, res):
    sums[0] = nums[0]  # base case for first sum
    # compute each sum from 1 to n
    for i in range(1, n):
        '''
        store next max sum: 
            case 1: sums[i-2] + nums[i] = new max sum found
            case 2: sums[i-1] = max is the same
            case 3: nums[i] = cases 1 and 2 are negative
        '''
        sums[i] = max(sums[i - 2] + nums[i], sums[i - 1], nums[i])

    n -= 1  # set n last index in nums
    while n > -1:
        # if: final num is reached, check if num at least 0 (avoids negatives)
        if sums[n] == nums[n]:
            if nums[n] > -1:
                res.append(nums[n])  # append final num
            return res[::-1]  # return result reversed
        # elseif: check if the next non-adjacent num is part of the current sum
        elif sums[n] == sums[n - 2] + nums[n]:
            res.append(nums[n])  # append num to result
            n -= 2  # move to check next non-adjacent num
        # else: check if current sum <= previous sum
        else:
            n -= 1  # nothing was added, skip current sum


def max_independent_set(nums):
    sums = [0] * len(nums)
    return find_max_set(nums, len(nums), sums, [])
