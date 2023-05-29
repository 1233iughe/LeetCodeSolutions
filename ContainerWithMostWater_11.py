'''
Both solutions are the same algorithm
1. Set pointers l and r
2. Calculate the area by (r-l)*min(height[l], height[r])
3. Move the smallest value pointer +/- 1 
4. Compare new area with old area and keep the max
        
Time O(n)
Space O(1)
'''    
#Two pointer (mine)
class Solution:
    def maxArea(self, height: List[int]) -> int:
        max_water = float('-inf')
        l = 0
        r = len(height) - 1
        while l < r:
            h = 0
            if height[l] > height[r]:
                h = height[r]
                area = (r - l) * h
                print(1, area)
                r -= 1
                if area > max_water:
                    max_water = area
            elif height[l] < height[r]:
                
                h = height[l] 
                
                area = (r - l) * h
                print(2, area)
                l += 1
                if area > max_water:
                    max_water = area
            else:
                h = height[l] 
                print(3)
                area = (r - l) * h
                l += 1
                if area > max_water:
                    max_water = area

            
            print(max_water)
        return max_water
#Two pointer by Neetcode
class Solution:
    def maxArea(self, height: List[int]) -> int:
        l, r = 0, len(height) - 1
        res = 0
        h = max(height)

        while l < r:
            res = max(res, min(height[l], height[r]) * (r - l))
            if height[l] < height[r]:
                l += 1
            elif height[r] <= height[l]:
                r -= 1
            
            if (r-l) * h <= res:
                break 
        return res
