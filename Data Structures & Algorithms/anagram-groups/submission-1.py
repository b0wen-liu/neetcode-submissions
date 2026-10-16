# from collections import Counter
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        map = {}
        for word in strs:
            c = str(sorted(word))
            if c in map.keys():
                map[c].append(word)
            else:
                map[c] = [word]
        return [words for words in map.values()]