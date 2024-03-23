class Solution:
    def maxArea(self, height: List[int]) -> int:
        '''
        [1] - [8] 
        [1,8,6,2,5,4,8,3,7]
        width = left - right
        max = 49

        two pointer
        left
        right
        height of container = min(left, right) 7 
        area = width * container_height

        
        '''

        max_area = 0
        left = 0
        right = len(height) - 1
        
        while left < right:
            # Calculate the width between the two bars
            width = right - left
            
            # Calculate the height of the container (minimum height between the two bars)
            container_height = min(height[left], height[right])
            
            # Calculate the area of the container
            area = width * container_height
            
            # Update max_area if the current area is greater
            max_area = max(max_area, area)
            
            # Move the pointer with the smaller height towards the other pointer
            if height[left] < height[right]:
                left += 1
            else:
                right -= 1
        
        return max_area