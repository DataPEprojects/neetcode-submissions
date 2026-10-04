class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:

        hash_map = {}
        difference = 0
        i = 0
        for num in nums:
            difference = target - num
            if difference not in hash_map:
                hash_map[num] = i
                i += 1
            else:
                return [hash_map[difference],i]
        print(hash_map)   
        






















