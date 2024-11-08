class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        # ans = [[1]]
        # iterate over the range of numrows - 1 bc we created the first row 
        # create a temp var 

        ans = [[1]]

        for i in range(numRows - 1):
            temp = [0] + ans[-1] + [0]
            row = []
            for j in range(len(ans[-1]) + 1):
                row.append(temp[j] + temp[j + 1])
            ans.append(row)
        return ans