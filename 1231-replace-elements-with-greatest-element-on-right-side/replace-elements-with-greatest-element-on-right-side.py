class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        # initiate the max_right as -1
        # iterate backwards from the end of the list
        # get the new_max from arr[i] and max_right
        # change arr[i] to be max_right
        # calculate the new max btwn max_right and new_max
        
        max_right = -1

        for i in range(len(arr) -1, -1, -1):
            new_max = arr[i]
            arr[i] = max_right
            max_right = max(max_right, new_max)

        return arr