class Solution:
    def intersection(self, nums1: list[int], nums2: list[int]) -> list[int]:
        numbers = []
        number_set = set(nums1)
        for num in nums2:
            if num in number_set and num not in numbers:
                numbers.append(num)
        return numbers