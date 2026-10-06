class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        count1 = {}
        count2 = {}
        for ch in s:
            if ch in count1:
                count1[ch] += 1
            else:
                count1[ch] = 1
        for char in t:
            if char in count2:
                count2[char] += 1
            else:
                count2[char] = 1
        if count1 != count2:
            return False
        
        return True