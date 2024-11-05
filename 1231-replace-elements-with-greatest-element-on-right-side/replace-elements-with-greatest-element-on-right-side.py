class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        # right_max = [-1]
        # compare max values while we iterate backwards
        # store the new_max in a variable
        # replace the last element with right_max

        right_max = -1

        for i in range(len(arr) -1, -1, -1):
            new_max = max(right_max, arr[i])
            arr[i] = right_max
            right_max = new_max
        
        return arr