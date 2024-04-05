class Solution:
    def transpose(self, matrix: List[List[int]]) -> List[List[int]]:
        
        result = []

        for col in range(len(matrix[0])):
            new_row = []

            for row in matrix:
                new_row.append(row[col])
            result.append(new_row)
        
        return result

