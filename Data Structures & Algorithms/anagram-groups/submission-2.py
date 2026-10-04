class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        from collections import defaultdict

        hash_ = defaultdict(list)

        for word in strs:
            count = [0]*26
            for letter in word:
                count[ord(letter) - ord('a')] +=1
            hash_[tuple(count)].append(word)
        return list(hash_.values())