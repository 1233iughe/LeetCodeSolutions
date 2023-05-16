class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        import heapq
        '''
        Possible to use heap

        Consequtive means a diference of 1
        [0,3,7,2,5,8,4,6,0,1]
        1. Create the array with remainders of a[i]-/+1
        [0,3,7,2,5,8,4,6,0,1] 0
        [-1,2,6,1,5,7,3,5,-1,0] -1
        [1,4,8,3,6,9,5,7,1,2] +1
        2. Create a HashMap on Sets 
        3. For each number check if it or one of its differences is already on a set
            3.1 If not create a new entry key(the value):set and add it
            3.2 If it is on set dont add it
            3.3 
        '''
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