'''
Algorithm (HashMap with bucket sort)
1. Create frequency table
2. Use bucket sort to tort the keys
3. Return the first 3


Algorithm (HashMap):
1. Create and empty dictionary
2. Loop through all the list and add each different integer as a key which value is increased by one each time that elelment is encountered.
3. Loop through the dictionary and check againsta a window of two the elements until you found the 2 greates values
or 
use max to found the biggest number, pop it and repeat
or 
create an array of length 0 and place each key at the index given by its value
        
Algorithm (HashMap):
1. Create an array len max(List) full of zeros
2. Increase by 1 the value at the index of corresponding to a given element of the list. Loop through all the elements
3. Loop through array checking using single window and checking against every element until we have the 2 biggest.

This solution only would work if all elements in the list are positive integers
 if len(nums) == 1:
    return num
frequency = [0]*(max(nums)+1
for num in nums:
    frequency[num] += 1

big_max = [frequency[0], 0]
small_max = [frequency[0], 0
for i, freq in enumerate(frequency):
    if freq > big_max[0]:
        small_max[0], small_max[1] = big_max[0], big_max[1]
        big_max[0], big_max[1] = freq, i
        continue
    elif freq > small_max[0]:
        small_max[0], small_max[1] = freq, i
        continue
    else:
        pas
return [small_max[1], big_max[1]]
     ''' 
#HashMap using bucket sort (optimal)
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        f = {}
        for num in nums:
            try:
                f[num] += 1
            except:
                f.setdefault(num, 1)

        x = [[] for i in range(len(nums)+ 1)]

        for key in f.keys():
            
            x[f[key]].append(key)

        clean = [j for i in x for j in i if i]
        
        return clean[-k:]

#HashMap (suboptimal over use of dictionaries O(k*n))
s Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        
        if len(nums) == 1:
            return nums
        frequencies = {}
        for num in nums:
            try:
                frequencies[num] += 1
            except:
                frequencies.setdefault(num, 1)
        
        commonest = set()
        x = [[key, frequencies[key]] for key in frequencies.keys()]
        while len(commonest) < k:
            big = [0,float(-inf)]
            j = 0
            for i, pair in enumerate(x):
                if pair[1] > big[1]:
                    big = pair
                    j = i
            commonest.add((x.pop(j))[0])
        return list(commonest)