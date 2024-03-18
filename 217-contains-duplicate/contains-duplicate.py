class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        # create a set
        # iterate through arr
        # if in the set, return true
        # else add the num to the set


        my_Set = set()

        for num in nums:
            if num in my_Set:
                return True
            else:
                my_Set.add(num)
        return False