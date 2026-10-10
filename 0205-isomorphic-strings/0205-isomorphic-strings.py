class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        mapping = {}
        reverse_mapping = {}

        for i in range(len(s)):
            char_s = s[i]
            char_t = t[i]

            if char_s in mapping:
                if mapping[char_s] != char_t:
                    return False
            else:
                mapping[char_s] = char_t

            if char_t in reverse_mapping:
                if reverse_mapping[char_t] != char_s:
                    return False
            else:
                reverse_mapping[char_t] = char_s

        return True
