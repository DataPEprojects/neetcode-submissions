class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hasher = {}
        for i,num in enumerate(nums):
            difference = target - num
            if difference not in hasher:
                hasher[num] = i
            else:
                return [hasher[difference],i]
