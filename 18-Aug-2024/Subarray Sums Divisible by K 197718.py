# Problem: Subarray Sums Divisible by K - https://leetcode.com/problems/subarray-sums-divisible-by-k/

class Solution:
    def subarraysDivByK(self, nums: List[int], k: int) -> int:
        dicc= defaultdict(int)
        summ=0
        dicc[0]= 1
        ans=0
        for i in range(len(nums)):
            summ+= nums[i]
            ans+= dicc[summ%k]
            dicc[summ%k]+=1
        return ans 
        