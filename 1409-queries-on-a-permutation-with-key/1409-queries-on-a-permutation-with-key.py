from collections import deque

class Solution:
    def processQueries(self, queries: List[int], m: int) -> List[int]:
        answer = []
        P = [i for i in range(1, m + 1)]

        for query in queries:
            idx = P.index(query)
            answer.append(idx)
            num = P.pop(idx)
            P = [num] + P

        return answer