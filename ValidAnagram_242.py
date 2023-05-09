'''
 Possible solutions
1. HashMap -> use it to create a map of letters and counts of those letters per string if they are the same then they are anagrams
Time complexity O(s+t) Space complexity O(s+t) n =s+t
2. Sorting -> Sort both strings and if they are equal the they are anagrams
Time complexity O(n*logn) Space complexity O(1) if optimized

Mine was HashMap with extra steps 
Time O(2*(s+t)) Space O(2*(s+t)) aprox due to sets (it is overstimated)
 '''       
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        s_set = set(s)
        t_set = set(t)
        if s_set == t_set:
            s_hash = {letter:s.count(letter) for letter in s_set}
            t_hash = {letter:t.count(letter) for letter in t_set}
            #print(s_hash, t_hash)
            for key in s_hash.keys():
                #print(s_hash[key])
                if s_hash[key] != t_hash[key]:
                    return False
            return True
        return False