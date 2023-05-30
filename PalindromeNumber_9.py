'''
Algorithm (two pointers):
1. Check if number is single digit or negative, it will be True or False respectively
2. Use 2 pointers to check left and right advancing by 1 until one is not equal or we finish
Time: O(n)
Space:O(n)?
'''
#Double pointer 
class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0:
            return False
        elif x < 10:
            return True
        else:
            x = str(x)
            l, r = 0, len(x)-1
            
            while l < r:
                if x[l] != x[r]:
                    return False
                l += 1
                r -= 1
            return True