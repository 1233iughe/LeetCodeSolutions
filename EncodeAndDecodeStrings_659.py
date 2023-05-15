class Solution:
    """
    @param: strs: a list of strings
    @return: encodes a list of strings to a single string.
    """
    def encode(self, strs):
        #print(1)
        encoded = ''
        for word in strs:
            encoded += f"{word}:;"
        return encoded

    """
    @param: str: A string
    @return: dcodes a single string to a list of strings
    """
    def decode(self, str):
        #print(1)
        decoded = ' '
        x = str.split(':;')
        return x
x = Solution()

test = ["we", "love", ":", "u"]

y = print(x.encode(test))
print(x.decode(y))