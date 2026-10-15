class Solution:
    def isPalindrome(self, s: str) -> bool:
        word = s.lower()
        clean_text = ""
        if word == " ":
            return True
        for ch in word:
            if ch.isalnum():
                clean_text += ch
        left = 0
        right = len(clean_text) - 1
        while left < right:
            if clean_text[left] == clean_text[right]:
                left += 1
                right -= 1
            elif clean_text[left] != clean_text[right]:
                return False
        return True
            