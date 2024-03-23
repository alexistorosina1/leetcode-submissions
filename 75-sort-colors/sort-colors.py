class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """

        left = 0
        middle = 0
        right = len(nums) - 1

        while middle <= right:
            if nums[middle] == 0:
                nums[middle], nums[left] = nums[left], nums[middle]
                left += 1
                middle += 1
            elif nums[middle] == 2:
                nums[middle], nums[right] = nums[right], nums[middle]
                right -= 1
            else:
                middle += 1        