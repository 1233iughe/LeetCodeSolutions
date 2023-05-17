'''
Algorithm (array):

'''
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

        

