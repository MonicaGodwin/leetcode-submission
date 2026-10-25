class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        words = s.split()

        if len(pattern) != len(words):
            return False

        mapping = {}
        word_mapping = {}

        for i in range(len(pattern)):
            ch = pattern[i]
            word = words[i]

            if ch in mapping:
                if mapping[ch] != word:
                    return False
            else:
                mapping[ch] = word

            if word in word_mapping:
                if word_mapping[word] != ch:
                    return False
            else:
                word_mapping[word] = ch

        return True