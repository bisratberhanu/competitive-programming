class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        candidatess =[]
        seen= set()
        def backTrack(summ,candidate):
            if summ> target:
                return
            if summ== target:
                sorted_check= sorted(candidate)
                tupled= tuple(sorted_check)
                if tupled not in seen:
                    candidatess.append(sorted_check)
                    seen.add(tupled)
            for val in candidates:
                candidate.append(val)
                
                backTrack(summ+val, candidate)
                candidate.pop()
        
        backTrack(0, [])
        return candidatess 


        