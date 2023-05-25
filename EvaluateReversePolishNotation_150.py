''''
Time: O(n)
Space: O(n)
'''
#Stack solution (mine)

class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        i=0
        while tokens:
            token = tokens.pop(0)
            print(token)
            if token not in {'+','-','/','*'}:
                #print(1)
                stack.append(int(token))
            else:
                op1 = stack.pop(-1)
                op2 = stack.pop(-1)
                if token == '+':
                    result = op1 + op2
                elif token == '-':
                    result = op2 - op1
                elif token == '/':
                    result = int(op2 / op1)
                else:
                    result = op1 * op2
                stack.append(result)
                #print(op1, token, op2, result)
            i += 1
        return stack[0]
#Stack solution by neetcode
class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        for c in tokens:
            if c == "+":
                stack.append(stack.pop() + stack.pop())
            elif c == "-":
                a, b = stack.pop(), stack.pop()
                stack.append(b - a)
            elif c == "*":
                stack.append(stack.pop() * stack.pop())
            elif c == "/":
                a, b = stack.pop(), stack.pop()
                stack.append(int(b / a))
            else:
                stack.append(int(c))
        return stack[0]
