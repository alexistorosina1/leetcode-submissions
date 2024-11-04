class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # create a dictionary that contains num and its index
        # as we iterate through the array we look for the target nums complement
        # if complement is not in the dictionary then place it into the dictionary
        # else return the complement and i

        nums_dict = {}

        for i, num in enumerate(nums):
            complement = target - num

            if complement in nums_dict:
                return [nums_dict[complement], i]

            nums_dict[num] = i
        
