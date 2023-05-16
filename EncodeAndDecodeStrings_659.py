'''
Algorithm (dynamic array and arrays):
1. Select a special character as spacer.
2. Loop throught each element of the list and add them to a string with the following format
n° of characters+separator+element
3. To decode check if element[i] is equal to separator 
    3.1 if it is stablish the end of the word by checking a[i-1] and add the value to i + 1 (j)
    3.2 Extract the charcter of the word by copying all elements from the string in the range a[i+1:j]
    3.3 Append to the output list
    3.4 Set i = j
    3.6 If not equal to separator add 1 to i
Encode:
n -> length of list
w -> length of average word
Time: O(n)
Space: O(n*(w+1+digits in number of characters))-> O(n*w)
Decode:
s_> length of string
Time: O(2/3s) -> O(s)
Space: O(n)
'''
class Solution:
    """
    @param: strs: a list of strings
    @return: encodes a list of strings to a single string.
    """
    def encode(self, strs):
        #print(1)
        encoded = ''
        for word in strs:
            encoded += f"{len(word)}#{word}"
        return encoded

    """
    @param: str: A string
    @return: dcodes a single string to a list of strings
    """
    def decode(self, strs):
        #print(1)
        decoded,i = [],0
        x=''
        while i < len(strs):
            if strs[i] =="#":
                j= i+1+int(strs[i-1])
                decoded.append(strs[i+1:j])
                i = j
                continue
            i += 1
        return decoded
    
x = Solution()

test = ["we", "love", "#", "u"]

y = x.encode(test)
print(y)
print(x.decode(y))