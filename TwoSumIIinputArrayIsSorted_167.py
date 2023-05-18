'''
Algorithm (complement searching/ one pointer one holder)
1. Loop while substracting the ith element to target
2. Check if difference is on numbers
3. If it is hold the value and index
4. Check until hold equals ith value

Time: O(n)
Space:O(1)

Algorithm (2 pointers):
1. Since the array is ordered it can be used as any sum of 2 numbers can be compared against target
2. If is > reduce the right pointer
3. If is < increase left pointer
4. Repeat until a[left]+a[right] == target

Time: O(n)
Space:O(1)
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
#One pointer and holder
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
        