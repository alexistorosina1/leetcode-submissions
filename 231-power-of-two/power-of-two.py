class Solution:
    def isPowerOfTwo(self, n: int) -> bool:

        ''' 
        using bitwise
        '''

        return n > 0 and (n & (n -1)) == 0
        