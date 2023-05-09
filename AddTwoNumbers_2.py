    '''
    Algorithm (brute force):
    1. Loop each element against all other elements 
    2. Check which will add up

    Algorithm (improved)
    1. Loop trought each element 
    2. Find difference with target
    3. Check if difference is in the array

    Corner cases -> current element is equal to the difference
    '''
#Using difference mapping
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