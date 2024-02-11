class Solution:
    def bestClosingTime(self, customers: str) -> int:
        before=[0]*(len(customers))
        after= [0]*(len(customers))
        acc1,acc2= 0,0
        for i in range(len(customers)):
            before[i]= acc1
            if customers[i]=='N':

                acc1+=1
            
        for i in range(len(customers)-1,-1,-1):
            if customers[i]=='Y':
                acc2+=1
            after[i]= acc2
        before.append(before[-1])
        after.append(0)
        
        
        val= float(inf)
        ans=-1
        for i in range(len(before)):
            cand= before[i]+ after[i]
            if cand< val:
                val= cand
                ans= i
        return ans 
        
            