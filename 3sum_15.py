'''
The problem is a slightly more complicated version of the 2 sum problem.
Original: [-1,0,1,2,-1,-4]
Complement to 0: [1,0,-1,-2,1,4]
For every num check if any other 2 two nums add to its complement:
Complements for complement of -1: [None,1,0,2,5]
Complements for complement of 0: [1,None,-1,2,1,4]
Complements for complement of 1: [0,-1,None,-3,0,3]
Complements for complement of 2: [-3,-2,-1,None,-3,2]
Complements for complement of -1: [0,1,0,None,5]
Complements for complement of -4: [5,-4,-6,-3,5,None]
        
Algorithm (Time: O(n²), Space O(n))
1. Sort the array
2. Loop throught the array checking if there are 2 num that add up 
to the complement.
3. If the next number is not equal to the current number set to pointers i+1 and len(array)-1
    3.1 If they add over the target decrease right by 1 
    3.2 If they add under the target increase left by 1
    3.3 If they cross break the loop
    3.4 If i == i+1 move to i+2 to avoid duplicates
'''

#Brute force solution that times out
class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        triplets = []
        x = []
        targets = [-nums[i] for i in range(len(nums))]
        #print(targets)

        for i,target in enumerate(targets):
            neo_nums = [nums[x] for x in range(len(nums)) if x != i]
            for j,num in enumerate(neo_nums):
                for k in range(len(neo_nums)):
                    if target-num == neo_nums[k] and k != j and {nums[i], num, target-num} not in x:
                        x.append({nums[i], num, target-num})
                        triplets.append([nums[i], num, target-num])
        return triplets          
# Two pointer solution by Neetcode (implementation is mine)
class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:

        nums.sort()
        n = len(nums)
        triplets = []

        for i,num in enumerate(nums):
            if i != 0 and nums[i-1] == num:
                continue
            j = i+1
            k = n-1
            while j < k:
                threeSum = num + nums[j] + nums[k]
                if threeSum == 0:
                    triplets.append([num, nums[j], nums[k]])
                    j += 1
                    while nums[j] == nums[j-1] and j < k:
                        j += 1
                    continue
                elif threeSum > 0:
                    k -= 1
                    continue
                else:
                    j += 1    
        return triplets