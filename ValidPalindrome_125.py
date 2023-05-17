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