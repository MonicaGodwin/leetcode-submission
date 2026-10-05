class Solution:
    def longestCommonPrefix(self, strs: list[str]) -> str:
        words = strs
        prefix = ""
        for ch in range(len(words[0])):
            for word in words:
                if ch >= len(word) or word[ch] != words[0][ch]:
                    return prefix
            prefix += words[0][ch]
        return prefix