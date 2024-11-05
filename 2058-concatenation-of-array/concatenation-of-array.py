class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        # arr = [1, 2, 1]
        # iterate twice and populate arr
        # ans = [1, 2, 1]
        # but the output has to be [1, 2, 1, 1, 2, 1]
        ans = []

        for _ in range(2):
            for num in nums:
                ans.append(num)
        
        return ans