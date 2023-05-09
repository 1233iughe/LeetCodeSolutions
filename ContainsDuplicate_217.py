'''
This problem is supposed to be solved using arrays, but a great number of solutions used sets or hash tables 
'''
#Strict array solution (times out)
class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:

        unique = []
        n = len(nums)
        for i in range(n // 2):
            #print(i, unique, )
            if nums[i] not in unique:
                unique.append(nums[i])
            else:
                return True
            if nums[n-i-1] not in unique:
                unique.append(nums[n - i - 1])
                continue  
            else:
                return True
            
        return False

#Set solution O(n) both space and time
class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        return len(set(nums)) != len(nums)
            
#Hash table (dictionary) solution O(n) both space and time
class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:

        unique = {}
        n = len(nums)
        if n  % 2 != 0: unique[str(nums[n // 2])] = nums[n//2]
        for i in range(n // 2):
            
            a = str(nums[i])
            b = str(nums[n-i-1])
            #print(i, unique, a, b)
            if a in unique:
                return True
            unique[a] = nums[i]
            if b in unique:
                return True 
            unique[b] = nums[n-i-1] 
            
            
        return False
