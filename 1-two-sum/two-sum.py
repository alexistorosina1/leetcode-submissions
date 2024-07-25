class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # create a hashmap
        # populate the map as you iterate
        # check if the complement is already in the hashmap
        # if so return the complement and the index

    
        hashmap = {}

        for i, num in enumerate(nums):
            complement = target - num

            if complement in hashmap:
                return [hashmap[complement], i]
            
            hashmap[num] = i