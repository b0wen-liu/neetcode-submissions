class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        map = {}
        counter = 0
        for num in nums:
            if target - num in map.keys():
                return [map[target - num], counter]
            map[num] = counter
            counter+=1