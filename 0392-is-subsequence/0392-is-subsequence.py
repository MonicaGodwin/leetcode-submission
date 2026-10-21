class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        i = 0 #s
        j = 0 #t
        # s = "abc"
        # t = "ahbgdc"
        while j < len(t) and i < len(s):
            if s[i] == t[j]:
                i += 1
                j += 1
            elif s[i] != t[j]:
                j += 1
        if i == len(s):
            return True
        return False
            