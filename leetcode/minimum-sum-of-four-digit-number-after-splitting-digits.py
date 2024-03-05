class Solution:
    def minimumSum(self, num: int) -> int:
        minval= float(inf)
        strnum= str(num)
        
        
        
        for i in range(len(strnum)):
            for j in range(i+1, 4):
                str1= strnum[i] + strnum[j]
                summ= min(int(str1), int(str1[::-1]))
                temp= ""
                for k in range(4):
                    if k != i and k!= j:
                        temp+= strnum[k]
                temp= min(int(temp), int(temp[::-1]))
                minval= min(minval, temp+summ)
        return minval

            
