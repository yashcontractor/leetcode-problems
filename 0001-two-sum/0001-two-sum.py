class Solution(object):
    def twoSum(self, nums, target):
        arr = {}

        for i, j in enumerate(nums):
            c = target-j

            if c in arr:
                return [arr[c],i]

            arr[j] = i