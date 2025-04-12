class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        '''
        s = "abcd", t = "abcde", e is not in s

        the new char in t, does not exist at all in s, 

        s = 'abcd', t = 'acbdd', is d the char? or is this invalid

        '''

        s_set = set()
        for c in s:
            s_set.add(c)
        

        for c in t: 
            if c not in s_set: # Lookup of O(c) * O(n), for every char in s
                return c

