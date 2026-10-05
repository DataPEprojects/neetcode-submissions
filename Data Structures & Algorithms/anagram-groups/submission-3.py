class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        from collections import defaultdict

        hash_ = defaultdict(list)

        for st in strs:
            count=[0]*26
            for letters in st:
                count[ord(letters)-ord("a")] +=1
            hash_[tuple(count)].append(st)
        return list(hash_.values())