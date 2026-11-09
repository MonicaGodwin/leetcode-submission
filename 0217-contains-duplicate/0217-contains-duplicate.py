class Solution:
    def containsDuplicate(self, nums: list[int]) -> bool:
        result = {}
        for num in nums:
            if num in result:
                result[num] += 1
                return True
            elif num not in result:
                result[num] = 1
        return False