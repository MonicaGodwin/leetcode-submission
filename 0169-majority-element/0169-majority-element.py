class Solution:
    def majorityElement(self, nums: list[int]) -> int:
        count = {}
        majority_count = 0
        for num in nums:
            if num in count:
                count[num] += 1
            else:
                count[num] = 1
            if count[num] > len(nums) / 2:
                majority_count = num
        return majority_count
        