class Solution:
    def isPalindrome(self, s: str) -> bool:
        # 2 pointers, left, right
        # while left < right
        # check if s[left] and s[right] is alphanumerical
        #  if s[left] !=s[right] return false

        left, right = 0, len(s) - 1

        while left < right:
            
            while left < right and not s[left].isalnum():
                left += 1
            
            while left < right and not s[right].isalnum():
                right -= 1
            
            if s[left].lower() != s[right].lower():
                return False
            
            left += 1
            right -= 1
        
        return True