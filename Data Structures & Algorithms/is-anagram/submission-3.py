class Solution:
    def isAnagram(self, s: str, t: str) -> bool:

        # word1 = sorted(s)
        # word2 = sorted(t)
        # print(f'{sorted(word1)} == {sorted(word2)}')
        if sorted(s) == sorted(t):
            return True
        else:
            return False