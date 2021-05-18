"""
Given an array N, we define its running sum as: N[i] = sum(N[0], N[1],...N[i]).
Return the running sum of N.

sample input:

- nums = [1,2,3,4]

sample output:

- result = [1, 3, 6, 10] ([1, 1+2, 1+2+3, 1+2+3+4])

"""


def runningSum(self, nums):
    """
    :type nums: List[int]
    :rtype: List[int]
    """
    s = 0
    i = 0
    l = len(nums)
    res = []
    while(i < l):
        s += nums[i]
        i += 1
        res.append(s)
    return res
