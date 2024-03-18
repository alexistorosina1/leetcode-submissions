class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # create a hash to store elements with their indices
        # check for complements when iterating
        # check if target - nums[i] exists in the hash
        # if it exists, return the indices of nums[i] and the complement from the hash
        # else add the current element to the hash

        hash = {}

        for i, num in enumerate(nums):
            complement = target - num

            if complement in hash:
                return [hash[complement], i]
            else:
                hash[num] = i

        return None



        