class Solution:
    def isPowerOfTwo(self, n: int) -> bool:

        ''' 
        recursively divide n /2 until it reaches 1 or it becomes not
        divisible
        '''

        if n == 1:
            return True

        if n % 2 != 0 or n == 0:
            return False

        return self.isPowerOfTwo(n/2) 
        