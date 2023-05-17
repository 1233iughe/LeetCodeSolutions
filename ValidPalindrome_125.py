'''
Algorithm (two pointers)
1. Loop through the str with 2 pointers
2. The first pointer starts at 0 the other at n-1
3. If both are alphanumerical check if they are equal. Return false if not
4. If one is not alphanumerical increment/decrement it by 1 until it is
5. After successful comparison increment/decrement by 1 each pointer.
6. Finish loop after both indexes are equal
7. Return true

Time: O(n)
Space: O(1) or O(n) depending on implementation

'''

#O(1) space by neetcode
class Solution:
    def isPalindrome(self, s: str) -> bool:
        l, r = 0, len(s) - 1
        while l < r:
            while l < r and not self.alphanum(s[l]):
                l += 1
            while l < r and not self.alphanum(s[r]):
                r -= 1
            if s[l].lower() != s[r].lower():
                return False
            l += 1
            r -= 1
        return True

    # Could write own alpha-numeric function
    def alphanum(self, c):
        return (
            ord("A") <= ord(c) <= ord("Z")
            or ord("a") <= ord(c) <= ord("z")
            or ord("0") <= ord(c) <= ord("9")
        )
#Two pointer by me 
class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = s.lower()
        new = ''
        #print(s)
        for c in s:
            if c in 'abcdefghijklmnopqrstuvwxyz0123456789':
                new = new + c

        n = len(new)
        #print(new)
        for i in range(n):
            print(new[i], new[n-i-1])
            if new[i] != new[n-i-1]:
                return False
            if i == n-1-i: break

        return True
#Built in based solution (mine)
class Solution:
    def isPalindrome(self, s: str) -> bool:
        abc = 'abcdefghijklmnopqrstuvwxyz0123456789'
        new = ''
        if s:
            s = s.lower()
            for c in s:
                if c in abc:
                    new += c
            if new != new[::-1]: return False
        return True