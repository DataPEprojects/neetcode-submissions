class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        hash_ = set()
        for num in nums:
            if num not in hash_:
                hash_.add(num)
            else:
                return True
        return False