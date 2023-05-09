    '''
    Algorithm (brute force):
    1. Loop each element against all other elements 
    2. Check which will add up
    Time: O(n²) 
    Space: O(1)
    
    Algorithm (improved)
    1. Loop trought each element 
    2. Find difference with target
    3. Check if difference is in the array
    Time: O(n)
    Space: O(n)

    Best solution:
    Use HashMap to implement a mapping val:index as you loop once trought the array.
    While this happens check for the complement as in the improved algorithm but in the map itself. Its guarantee 
    you will have the 1st element in the HashMap when you get to the second element
    Corner cases -> current element is equal to the difference
    
    '''
#Using difference mapping (HashMap using a list)
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        copy_nums = nums.copy() 
        for i,num in enumerate(nums):
            diff = target - num
            copy_nums.pop(0)
            if diff in copy_nums:
                if diff == nums[i]:
                    nums[i] = diff +1
                return [i, nums.index(diff)]

#Brute force solution looping trough the array
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for i,num in enumerate(nums):
            for j, other in enumerate(nums):
                if i != j:
                    if num + other == target:
                        return [i, j]