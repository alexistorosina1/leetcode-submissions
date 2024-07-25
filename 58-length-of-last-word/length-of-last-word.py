class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        # iterate from the end of the string
        # create a variable to store the length
        # if i = " " skip
        # if i != " " increment length


        i, length = len(s) - 1, 0

        while i >= 0 and s[i] == " ":
            i -= 1
        
        while i >= 0 and s[i] != " ":
            length += 1
            i -= 1
        
        return length