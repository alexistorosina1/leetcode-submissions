class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # iterate through s and t
        # create 2 dictionaries containing each char and char count
        # compare dictionaries is dict_s == dict_t return true
    
        dict_s = {}
        dict_t = {}

        if len(s) != len(t):
            return False

        for char in s:
            dict_s[char] = dict_s.get(char, 0) + 1

        for char in t:
            dict_t[char] = dict_t.get(char, 0) + 1
        
        return dict_t == dict_s

        print(dict_s)