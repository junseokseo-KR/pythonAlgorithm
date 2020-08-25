"""
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for i in range(len(nums)):
            for j in range(i+1,len(nums)):
                if nums[i]+nums[j]==target:
                    return [i,j]

Runtime : 5956ms O(n^2)
Memory : 14.8 MB
"""


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        d = {}

        for i in range(len(nums)):
            lookup = target - nums[i]
            if lookup in d:
                return [i, d[lookup]]
            else:
                d[nums[i]] = i
        return [0, 0]
