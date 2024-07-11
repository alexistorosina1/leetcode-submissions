class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # place every char of list s into a dictionary
        # check if char in list t is in list s
        # return true if so
        
        hash_s = {}
        hash_t = {}

        for char in s:
            hash_s[char] = hash_s.get(char, 0) + 1

        for char in t:
            hash_t[char] = hash_t.get(char, 0) + 1

        return hash_s == hash_t 