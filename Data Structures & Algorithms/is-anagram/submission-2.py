class Solution:
    def isAnagram(self, s: str, t: str) -> bool:

        word1 = sorted(s)
        word2 = sorted(t)
        # print(f'{sorted(word1)} == {sorted(word2)}')
        if sorted(word1) == sorted(word2):
            return True
        else:
            return False