class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        # start at the end of the arr
        # if char == " " skip
        # if char is a letter then increment length by 1
        # return length 

        i, length = len(s) -1, 0

        while i >= 0 and s[i] == " ":
            i -= 1
        
        while i >= 0 and s[i] != " ":
            length += 1
            i -= 1

        return length