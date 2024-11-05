class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        # 2 pointers to compare both strings
        # if i == j then move i pointer up
        # j pointer will always move up
        # return true if i finished iterating
        i, j = 0, 0

        while i < len(s) and j < len(t):
            if s[i] == t[j]:
                i += 1
            j += 1
        
        return i == len(s)