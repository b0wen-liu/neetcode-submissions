class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        map = {}
        for num in nums:
            map[num] = map.get(num, 0) + 1
        freqSorted = sorted(map.keys(),key = lambda x: map[x], reverse=True)
        return freqSorted[:k]