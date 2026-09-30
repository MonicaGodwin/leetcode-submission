class Solution:
    def isValid(self, s: str) -> bool:
        strng = s
        stack = []
        dictn = {")": "(", "]": "[", "}": "{"}
        for char in strng:
            if char == "(" or char == "[" or char == "{":
                stack.append(char)
            elif char == ")" or char == "]" or char == "}":
                expected = dictn[char]
                if stack == []:
                    return False
                top_item = stack.pop() 
                if expected != top_item: 
                    return False
        if stack == []:
            return True
        else:
            return False