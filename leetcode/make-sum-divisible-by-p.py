class Solution:
    def minSubarray(self, nums: List[int], p: int) -> int:
        dic= {0:-1}
        ans= len(nums)
        mod=p
        summ= sum(nums)
        p= summ%p
        print(mod)
        print(p)
        if p==0: return 0
        acc=0
        pref= [0]* len(nums)
        for i in range(len(nums)):
            acc+= nums[i]
            pref[i]= acc
        print(pref)
        acc=0
        for i in range(len(nums)):
            acc+= nums[i]
            if (acc %mod - p )%mod in dic:
                ans= min(ans, i- dic[(acc %mod - p )%mod ])
            dic[acc%mod]=i
        print(dic)
        if ans== len(nums):
            return -1
        return ans 
