'''
Algorithm (complement searching/ one pointer one holder)
1. Loop while substracting the ith element to target
2. check if difference is on numbers
2. 

'''
#Two pointers, based in Neetcode solution 
class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:

        l,r = 0, len(numbers) -1
        while l != r:
            if numbers[l] + numbers[r] < target:
                l += 1
                continue
            elif numbers[l] + numbers[r] > target:
                r -= 1
            else:
                return [l+1, r+1]
        return False
#One pointer
class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:

        pointer1 = None
        holder = 0
        n = len(numbers)
        for i in range(n):
            diff = target - numbers[i]
            if diff in numbers and pointer1 == None: 
                #print(1)
                pointer1 = i
                holder = diff
                continue
            if pointer1 != None and numbers[i] == holder: 
                #print(2)
                return [pointer1+1, i+1]
        