class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        # given an arr nums 
        # remove val from nums
        # return number of elements in the arr

        # loop through arr
        # if num val == k 
        # remove num
        # return length + 1
        k = 0

        for i in nums:
            if i != val:
                nums[k] = i
                k += 1
        
        return k