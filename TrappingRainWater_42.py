class Solution:
    def trap(self, height: List[int]) -> int:
        '''
        Analysis:
        1. Water starts being trapped when it is between two numbers > 0
        2. Water in any given formation has its maximum when between the 2 equal biggest numbers
        
        Algorithm:

        '''
        l, r =0, len(height)-1
        max_left, max_right = height[l], height[r]  
        water = 0

        while l < r:
            print(f'r: {r}, l: {l}, ml: {max_left}, mr: {max_right}')
            if max_left <= max_right:
                l += 1
                if height[l] > max_left:
                   max_left = height[l]
                water += max_left - height[l]
                
            else:
                r -= 1  
                if height[r] > max_right:
                   max_right = height[r]
                water += max_right - height[r]
                 
        
        return water

        