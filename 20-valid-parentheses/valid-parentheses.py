class Solution:
    def isValid(self, s: str) -> bool:
        # stack
        # need a map with correspondig closing brackets
        
        stack = []
        map = {
            ")": "(",
            "}": "{",
            "]": "["
        }

        for char in s:
            if char in map:
                if stack and stack[-1] == map[char]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(char)
        
        return not stack


                    
