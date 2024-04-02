class Solution:
    def flipAndInvertImage(self, image: List[List[int]]) -> List[List[int]]:
        '''
        we need to flip first then invert
        assuming only 0's and 1's
        step 1: flip
        [1, 1, 0] -> [0, 1, 1]
        step 2: invert
        [0, 1, 1] -> [1, 0, 0]

        '''

        for row in image:
            left, right = 0, len(row) - 1

            while left <= right:
                row[left], row[right] = row[right], row[left]

                left += 1
                right -= 1

            for i in range(len(row)):
                row[i] = 1 - row[i]
        
        return image
        