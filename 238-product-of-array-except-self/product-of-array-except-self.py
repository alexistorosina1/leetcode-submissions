class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        left_products = [1] * len(nums)
        
        left_product = 1
        
        for i in range(len(nums)):
            left_products[i] = left_product
            left_product *= nums[i]
        
        right_product = 1
        
        for i in range(len(nums) - 1, -1, -1):
            left_products[i] *= right_product
            right_product *= nums[i]
        
        return left_products