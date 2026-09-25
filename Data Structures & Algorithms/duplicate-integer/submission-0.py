class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        hash_ = set()
        for n in nums:
            if n in hash_:
                return True
            else:
                hash_.add(n)
        return False