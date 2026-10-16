class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        sMap = {}
        for c in s:
            sMap[c] = sMap.get(c, 0) + 1
        for c in t:
            try:
                sMap[c] = sMap.get(c) - 1
            except Exception:
                return False
        for i in sMap.values():
            if i != 0:
                return False
        return True