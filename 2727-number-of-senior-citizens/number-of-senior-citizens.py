class Solution:
    def countSeniors(self, details: List[str]) -> int:
        # we can start the iteration after the char or index 10
        count = 0
        for d in details:
            age = int(d[11:13])
            if age > 60:
                count += 1
        return count