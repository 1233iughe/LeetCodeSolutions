'''
Algorithm (using lookup array):
1. Loop through array while multiplying in a factorial like fashion from both ends. Store
the results in two separate arrays. Each index must contain the cumulative product 'til that 
number depending on the direction. 
2.Loop through the indexes of those arrays simultineusly so you can get the cumulative product exactly before that number
on each array.
3. Multiply those and append to answer array.

Corner cases:
1. Getting to the beggining or end of the array will imply that the result only needs one of the lookup arrays.
Time: O(2n) -> O(n)
Space:  O(2n) -> O(n)

Algorithm (using answer array as lookup):
1. Loop through all values except n-1 on nums while making the cumulative product and storing it in i+1 skiping i = 0 in the answer array
2. Loop again in reverse order skipping i = n-1 in the answer array and i = 0 in nums. Multiply the cumulative product against the value contain in 
the cell.
Time: O(2n) -> O(n)
Space:  O(1)
'''
#Using array for lookup
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
#Storing values on site
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        m = n - 1
        answer = [1]
        cumulator = 1
        for i in range(n-1):
            cumulator *= nums[i]
            answer.append(cumulator)
        

        cumulator = 1

        for i in range(n-1, 0, -1):
            cumulator *= nums[i]
            
            answer[i-1] = answer[i-1] * cumulator
            

        return answer