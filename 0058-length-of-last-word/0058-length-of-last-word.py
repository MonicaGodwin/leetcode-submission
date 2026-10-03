class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        word = s
        word = word.strip()
        splitted = word.split(" ")
        last_word = splitted[-1]
        len_lastword = len(last_word)
        return len_lastword
