class Solution(object):
    def twoSum(self, nums, target):
        positions = {}

        for i, num in enumerate(nums):
            complement = target-num

            if complement in positions:
                return [positions[complement],i]

            positions[num] = i