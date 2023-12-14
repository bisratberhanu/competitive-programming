class Solution:
    def sumEvenAfterQueries(self, nums: List[int], queries: List[List[int]]) -> List[int]:
        init_sum=0
        for val in nums:
            if val%2==0:
                init_sum+=val
        ans=[]
        for query in queries:
            temp= nums[query[1]]+ query[0]
            if temp%2==0:
                if nums[query[1]]%2==0:
                    init_sum+= query[0]
                else:
                    init_sum+= temp
            else: # if temp is odd
                if nums[query[1]]%2==0:
                    init_sum-= nums[query[1]]
            nums[query[1]]= temp
            ans.append(init_sum)
        return ans 