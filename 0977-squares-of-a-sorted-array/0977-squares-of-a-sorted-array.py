class Solution:
    def sortedSquares(self, nums: list[int]) -> list[int]:
        squared_list = []
        for num in nums:
            squre = num * num
            squared_list.append(squre)
            squared_list.sort()
        return squared_list
