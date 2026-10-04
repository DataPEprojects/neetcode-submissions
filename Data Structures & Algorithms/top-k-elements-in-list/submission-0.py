class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        from collections import defaultdict
        res = defaultdict(int)

        for num in nums:
            res[num] +=1
        return sorted(res, key=res.get, reverse=True)[:k]