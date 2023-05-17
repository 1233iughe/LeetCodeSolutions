'''
Algorithm (dynamic array):
1. Push is implemented as appending to the end of array
2. Pop is implemented as eliminating the value of last index
3. Top is implemented as accessing the last value
4. getMin is implemented with a lookup array that collects each value smallest or equal 
than the last and pops its last value each time it matches the poped value of the stack.
Time: O(1)
Space: O(n)

'''
#Mine
class MinStack:

    def __init__(self):
        self.stack = []
        self.minimal = []
        

    def push(self, val: int) -> None:
        #print(1)
        self.stack.append(val)
        if self.minimal:
            if val <= self.minimal[-1]: self.minimal.append(val)
        else: 
            self.minimal.append(val)

    def pop(self) -> None:
        if self.stack.pop(-1) == self.minimal[-1]: self.minimal.pop(-1)
        

    def top(self) -> int:
        return self.stack[-1]
        

    def getMin(self) -> int:
        return self.minimal[-1]
#Neetcode
class MinStack:
    def __init__(self):
        self.stack = []
        self.minStack = []

    def push(self, val: int) -> None:
        self.stack.append(val)
        #
        val = min(val, self.minStack[-1] if self.minStack else val)
        self.minStack.append(val)

    def pop(self) -> None:
        self.stack.pop()
        self.minStack.pop()

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return self.minStack[-1]

        

