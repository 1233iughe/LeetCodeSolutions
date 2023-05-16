'''
Algorithm (heap):
1. Create set of the list given
2. Use min/max heap to check if every next -prev number is equal to 1
3. Add 1 to counter and proceed or simply add counter to sequence and set counter to 1
4. Return mac element in sequence
Time: O(n)
Space: O(n)

Algorithm (set)
1. Create set of the list given
2. loop throught the set
3. if the previous element is in there (n-1) it will continue the sequence
4. If ended compare to previous biggest sequence
Time: O(n)
Space: O(n)

'''
#Heap
class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        import heapq

        if len(nums) <= 1:
            return len(nums)
        nums = list(set(nums))
        heapq.heapify(nums)
        sequences = set()
        prev = heapq.heappop(nums)
        next = 0
        counter = 1
      
        while nums:
            next = heapq.heappop(nums)
            print(prev,next, counter)
            if abs(prev-next) == 1:
                counter += 1
                prev = next
                if not nums:
                    sequences.add(counter)
                    break
                continue
            
            sequences.add(counter)
            counter = 1
            prev = next
        print(sequences)
        if not sequences:
            return 1
        
        return max(sequences)

#No heap by chappy1
class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        #Setting a variable to keep track of the longest sequence
        longest = 0
        #Setting set to keep track of unique elements
        num_set = set(nums)

        #Looping through each individual element
        for n in num_set:
            #Checking if the previous element in the sequence is in set
            if (n-1) not in num_set:
                #Mrking the start of a sequence
                length = 1
                #While the sequence continues the elements n+1 exist in set
                while (n+length) in num_set:
                    length += 1
                #Save the biggest number between the previous longest and the current sequence
                longest = max(longest, length)
        #Returns the longest sequence
        return longest