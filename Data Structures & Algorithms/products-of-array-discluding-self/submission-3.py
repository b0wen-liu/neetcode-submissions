class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        front = []
        back = []
        out = []
        # go forwards and backwards?
        for num in nums:
            try:
                front.append(front[-1] * num)
            except IndexError:
                front.append(num)
        for num in nums[::-1]:
            try:
                back.append(back[-1] * num)
            except IndexError:
                back.append(num)
        back = back[::-1]
        out.append(back[1])
        for i in range(len(nums) - 2):
            out.append(front[i] * back[i + 2])
        out.append(front[-2])
        # print(front, back, out)
        return out