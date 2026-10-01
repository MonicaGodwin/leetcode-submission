class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0:
            return False
        converted = str(x)
        left = 0
        right = len(converted)-1
        while left < right:
            if converted[left] != converted[right]:
                return False
            left += 1
            right -= 1
        return True