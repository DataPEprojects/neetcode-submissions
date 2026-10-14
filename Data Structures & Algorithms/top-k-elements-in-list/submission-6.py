class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        from collections import defaultdict
        count = defaultdict(int)
        for n in nums:
            count[n] += 1
        sorted_elements = sorted(count.items(), key=lambda x:x[1],reverse = True)

        top_k = [item[0] for item in sorted_elements[:k]]

        return top_k

