'''
    
'''
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        m = n - 1
        right = []
        left = []
        multiplier = 1
        inverse = 1
        answer = []
        for i in range(n):
            multiplier *= nums[i]
            right.append(multiplier)
            inverse *= nums[m-i]
            left.append(inverse)
        
        for i in range(n):
            j = i - 1
            k = n - 2 - i
            if j < 0:
                answer.append(left[k])
                continue
            if k < 0:
                answer.append(right[j])
                continue
            answer.append(left[k]*right[j])
            
        return answer