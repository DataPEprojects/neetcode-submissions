class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        dictionnary = {}

        for i,words in enumerate(strs):
            word_sorted = "".join(sorted(words))
            if word_sorted not in dictionnary:
                dictionnary[word_sorted] = []
            dictionnary[word_sorted].append(words)

        return list(dictionnary.values())