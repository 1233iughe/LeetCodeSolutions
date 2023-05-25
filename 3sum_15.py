#Brute force solution that times out
class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
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
        '''
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
        