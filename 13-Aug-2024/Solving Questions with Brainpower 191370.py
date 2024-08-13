# Problem: Solving Questions with Brainpower - https://leetcode.com/problems/solving-questions-with-brainpower/

class Solution:
    def mostPoints(self, questions: List[List[int]]) -> int:
        
        @cache
        def dpp(i):
            if i >= len(questions):
                return 0
            
            next= i+ questions[i][1] +1 
            
            return max(questions[i][0] + dpp(next), dpp(i+1) )
        
        return dpp(0)