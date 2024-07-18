class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        # max_right = -1
        # iterate through the arr from the end
        # store the current element in a variable
        # replace that element with max_right
        # get the max from max_right and current variable

        max_right = -1

        for i in range(len(arr) -1, -1, -1):
            current = arr[i]
            arr[i] = max_right
            max_right = max(current, max_right)

        return arr 