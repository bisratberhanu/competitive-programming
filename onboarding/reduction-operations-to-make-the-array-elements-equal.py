class Solution:
    def reductionOperations(self, nums: List[int]) -> int:
        minelement= min(nums)
        dic= Counter(nums)
        lis=[]
        for val in dic:
            if val!= minelement:
                lis.append([val,dic[val]])
        lis.sort(reverse=True)
        ans=0
        acc=0
        for val in lis:
            ans+= acc+ val[1]
            acc+=val[1]
        return ans 
        