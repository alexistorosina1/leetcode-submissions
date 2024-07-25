class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        # use two pointers
        # if both pointers == the same 
        # move s pointer 
        # t pointer moves regardless


        i, j = 0, 0

        while i < len(s) and j < len(t):
            if s[i] == t[j]:
                i += 1
            j += 1

        return i == len(s)