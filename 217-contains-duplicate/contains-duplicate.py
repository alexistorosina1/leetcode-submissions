class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        # create a set?
        # iterate through nums array and place in set
        # if num is in set return True
        # else populate set and return False

        nums_set = set()
        for num in nums:
            if num in nums_set:
                return True
            else:
                nums_set.add(num)
        return False
            
