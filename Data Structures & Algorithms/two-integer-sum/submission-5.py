class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hash_ = {}
        for i,num in enumerate(nums):
            difference = target - num
            if difference not in hash_:
                hash_[num] = i
            else:
                return [hash_[difference],i]