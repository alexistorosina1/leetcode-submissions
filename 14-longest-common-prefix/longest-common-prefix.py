class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        # ans = ""
        # iterate through list of strings
        # for every first char of each str
        # if == then we add to ans
        # move to next char

        ans = ""

        for i in range(len(strs[0])):
            for char in strs:
                if i == len(char) or char[i] != strs[0][i]:
                    return ans
            ans += strs[0][i]
        return ans

            
            