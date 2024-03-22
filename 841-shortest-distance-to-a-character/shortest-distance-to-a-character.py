class Solution:
    def shortestToChar(self, s: str, c: str) -> List[int]:
        '''
        [11, 11, 11, 0, 11, 0, 0, 11, 11, 11, 11, 0]
        '''

        answer = []
        indx_of_c = []
        for i in range(len(s)):
            if s[i] != c:
                answer.append(len(s))
            else:
                indx_of_c.append(i)
                answer.append(0)
        for i in range(len(answer)): # the indexs 0 1 2 3 4 5 ... 11
            shortest_dist = len(s)
            for n in indx_of_c:
                dist = abs(n-i)
                if(shortest_dist > dist):
                    shortest_dist = dist
            answer[i] = shortest_dist # updating the values here directly
        return answer










    