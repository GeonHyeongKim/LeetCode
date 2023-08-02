class Solution:
    def numberOfMatches(self, n: int) -> int:
        answer = 0

        while n > 1:
            mod = n // 2 

            if n % 2 == 0: # 짝수
                n = mod
            else: # 홀수
                n -= mod
            
            answer += mod

        return answer