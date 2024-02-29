class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        sortedcandi= sorted(candidates)
        if sum(sortedcandi)< target: return []
        arr=[]
        seen= set()
        def backTrack(index, lis,summ):
            if summ== target:
                #tupled= tuple(lis)
                
                #if tupled not in  seen:
                arr.append(lis[:])
                  #  seen.add(tupled )
                #return 
            if summ> target:
                return False 
            
            
            for i in range(index, len(candidates)):
                if i>index and sortedcandi[i]== sortedcandi[i-1]:
                    continue  
                lis.append(sortedcandi[i])
                summ+= sortedcandi[i]
                
                if backTrack(i+1, lis, summ)== False:
                    lis.pop()
                    summ-= sortedcandi[i]
                    break

                lis.pop()
                summ-= sortedcandi[i]
        
        backTrack(0,[],0)
        return arr 
            