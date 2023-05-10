'''
Algorithm (HashMap suboptimal):
1. Create a footprint list to store all the different word footprints
2. Create a HashMap (letter:count) for the letters of the first word
and append to the footprint list
3. Loop through the rest of the words
    3.1 Create HashMap
    3.2 Compare values with each stored hashmap if not found
    then add to footprint list or if found add to the corresponfind sublist.
    3.3 Sublists of output correspond to the indexes of their footprints in the otyher array
Time:O(len(strs)*len(word)) so poibly n² or >
Space: O(n)

Algorithm (Sorting):
1. Sort every word O(n*logn) * O(m) -> O(m*n*logn)
2. Check if that string is in our lookup list
    2.1 If in then add at the appropiate location on output
    2.2 If not then add to set and add new sublist to output

Time: O(m*n*logn)
Space: O(n)

#HashMap (Optimal)
1. Create a dictionary which default value for very new key is an empty list
2. Loop through all words
    2.1 Per word create a signature array of 26 zeroes to store its footprint
    2.2 Add 1 to the index correponding a given letter for all letters in the word
    2.3 Use the signature as a key by converting it to a tuple
        2.3.1 Append to the corresponding part of the HashMap
Time: O(n*m) n = average length of word and m = length of strs
Space: O(keys + m)
'''
#HashMap(Optimal)
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        ans = collections.defaultdict(list)

        for s in strs:
            count = [0] * 26
            for c in s:
                count[ord(c) - ord("a")] += 1
            ans[tuple(count)].append(s)
        return ans.values()


#HashMap (Suboptimal)
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        footprints = []
        output =[[]]
        for word in strs:
            footprint = {}
            
            for letter in word:
                footprint[letter] = 1 + footprint.get(letter, 0)

            if not footprints:
                footprints.append(footprint)
                output[footprints.index(footprint)].append(word)
                continue

            if footprint in footprints:
                output[footprints.index(footprint)].append(word)
                continue
            footprints.append(footprint)
            output.append([word])
            #print(output)
            #print(footprints)
        return output 
#Sorting solution

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        '''

        '''
        footprints = []
        output =[[]]

        for word in strs:
            footprint = ''.join(sorted(word))
            
            if not footprints:
                footprints.append(footprint)
            
            if footprint in footprints:
                output[footprints.index(footprint)].append(word) 
                continue

            footprints.append(footprint)
            output.append([word])

        
        return output