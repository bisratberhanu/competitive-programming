class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        ans=[]
        prefix_product=[1]*(len(nums)+1)
        sufix_product=[1]*(len(nums)+1)
        j=len(nums)
        for i in range(len(nums)):
            prefix_product[i+1]= prefix_product[i]*nums[i]
            sufix_product[j-1]= sufix_product[j]*nums[j-1]
            
            j-=1
            
        print(sufix_product)
        print(prefix_product)
        for i in range(len(nums)):
            ans.append(prefix_product[i]*sufix_product[i+1])
        return ans 
        