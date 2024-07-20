class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # create a hashmap
        # iterate through nums
        # check if the complement is in nums
        # return if so, if not add to hash

        hashmap = {}

        for i, num in enumerate(nums):
            complement = target - num

            if complement in hashmap:
                return [hashmap[complement], i]

            hashmap[num] = i