class Solution:
    def sortArrayByParity(self, nums: List[int]) -> List[int]:
        '''
        two pointers, one at the start and one at the end
        we use modulo to find out if the number is even or odd
        if the end pointer is even we swap with the start pointer, first += 1
        else we move pointer += 1
        [3, 1, 2, 4]
        ^         ^ 
        [4, 1, 2, 3]
            ^  ^ 
        '''

        first = 0
        second = len(nums) - 1

        
        while first < second:
            while first < second and nums[first] % 2 == 0:
                first += 1
            
            while first < second and nums[second] % 2 == 1:
                second -= 1

            nums[first], nums[second] = nums[second], nums[first]

            first += 1
            second -= 1
        
        return nums
