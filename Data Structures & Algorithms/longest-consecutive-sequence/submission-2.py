class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:
            return 0
        noDupes = set(nums)
        sortedNums = sorted(list(noDupes))
        print(sortedNums)
        runMax = 1
        truMax = 0
        lastNum = sortedNums[0]
        debugList = [lastNum]
        for num in sortedNums[1:]:
            if num - lastNum == 1:
                runMax += 1
                debugList.append(num)
            else:
                # print(debugList)
                debugList = []
                truMax = max(runMax, truMax)
                runMax = 1
            lastNum = num
        truMax = max(truMax, runMax)
        return truMax