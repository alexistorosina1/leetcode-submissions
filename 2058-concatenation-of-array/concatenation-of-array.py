class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        # create ans arr
        # loop through nums twice
        # append num to ans arr []

        ans = []
        for i in range(2):
            for num in nums:
                ans.append(num)
        
        return ans

