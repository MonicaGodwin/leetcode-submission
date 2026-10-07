class Solution:
    def firstUniqChar(self, s: str) -> int:        
        char = {}
        for ch in s:
            if ch in char:
                char[ch] += 1
            else:
                char[ch] = 1
        for i in range(len(s)):
            if char[s[i]] == 1:
                return i
        return -1


