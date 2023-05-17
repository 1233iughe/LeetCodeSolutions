'''
Algorithm (stack)

1. Loop through each element in the string
2. Per element check if it is left or right braket 
    2.1 We could use a map left:right, so if not in map means its right
    2.2 If left push into stack (append)
    2.3 If right pop from stack and check if right is equal to the value of left in map
    2.4 If it is not end the function, continue if it is true

Example:
()[{()()}]
>(
()
>[{(
()
>[{(
()
>[{
{}
>[
[]
>
Valid

Time: O(n)
Space: O(n)
'''

#Hash map by neetcode
class Solution:
    def isValid(self, s: str) -> bool:
        Map = {")": "(", "]": "[", "}": "{"}
        stack = []

        for c in s:
            if c not in Map:
                stack.append(c)
                continue
            if not stack or stack[-1] != Map[c]:
                return False
            stack.pop()

        return not stack
#HashMap by me :D
class Solution:
    def isValid(self, s: str) -> bool:
        
        brackets = {'(':')', '[':']', '{':'}'}
        stack = []
        if s[0] not in brackets:return False

        for elem in s:
            if elem in brackets:
                stack.append(elem)
            else:
                if not stack: return False
                if brackets[stack[-1]] != elem: return False
                stack.pop(-1)      
        
        return not stack
