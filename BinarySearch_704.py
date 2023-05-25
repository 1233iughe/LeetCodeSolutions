class Solution:
    def search(self, nums: List[int], target: int) -> int:
        if not nums or target > nums[-1] or target < nums[0]:
            return -1


        index = [i for i in range(len(nums))]
        while len(nums) > 1:
            mid = len(nums) // 2
            print(nums, index, mid)
            if target > nums[mid]: 
                nums = nums[mid + 1:]
                index = index[mid +1:]
                continue
            elif target < nums[mid]:
                nums = nums[:mid]
                index = index[:mid]
                continue
            else:
                return index[mid]
        #print(nums, index)
        if nums[0] == target: return index[0]
        return -1

class Solution(object):
    def search(self, nums, target):
        left = 0
        right = len(nums) - 1
        
        while left <= right:
            mid = (left + right) // 2
            
            if nums[mid] == target:
                return mid
            elif nums[mid] < target:
                left = mid + 1
            else:
                right = mid - 1
        
        return -1
        