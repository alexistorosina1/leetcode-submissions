class Solution:
    def isValid(self, s: str) -> bool:
        # ["()"]
        stack = []
        closing_bracket = {
            ")": "(",
            "]": "[",
            "}": "{"
        }

        for char in s:
            if char in closing_bracket:
                if stack and stack[-1] == closing_bracket[char]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(char)
        return True if not stack else False
            
            
