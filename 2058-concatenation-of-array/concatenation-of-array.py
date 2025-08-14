class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        # returning a new arr with the length of 2n
        # loop through the arr twice and add the elements to the new arr
        ans = []
        for i in range(2):
            for num in nums:
                ans.append(num)
        
        return ans
