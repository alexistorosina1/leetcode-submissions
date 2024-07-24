class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # use a hashmap to keep track of each char in s
        # use a hashmap to keep track of each char in t
        # compare both
        hashmap_s = {}
        hashmap_t = {}
        
        for char in s:
            hashmap_s[char] = hashmap_s.get(char, 0) + 1
        
        for char in t:
            hashmap_t[char] = hashmap_t.get(char, 0) + 1

        return hashmap_s == hashmap_t
