class Solution:
    def moveZeroes(self, nums: list[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        left = 0
        current_val = 0
        while current_val < len(nums):
            if nums[current_val] == 0:
                current_val += 1
            elif nums[current_val] != 0:
                nums[left], nums[current_val] = nums[current_val], nums[left]
                left += 1
                current_val += 1