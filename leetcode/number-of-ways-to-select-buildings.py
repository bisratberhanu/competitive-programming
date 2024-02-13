class Solution:
    def numberOfWays(self, s: str) -> int:
        def helper(s, val):
            val_count= s.count(val)
            prev=0
            acc,temp,ans=0,0,0
            for letter in s:
                if int(letter)==int(val):

                    acc+=1
                    
                else:
                    temp+= acc
                    ans+=  (acc)*(val_count-acc)
            return ans

        if "0" not in s:
            return 0
        if "1" not in s:
            return 0
        
        return helper(s,"0") + helper(s,"1")
        
        