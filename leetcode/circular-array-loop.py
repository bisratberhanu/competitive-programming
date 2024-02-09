class Solution:
    def circularArrayLoop(self, nums: List[int]) -> bool:
        # two dictionaries for the postive and the negative, checking for redundancy in the dictionaries
        def traverse(initnode, finalnode,dic):
            temp= initnode
            while dic[initnode]!= finalnode:
                if dic[initnode] in dic and dic[initnode]!= initnode:
                    initnode= dic[initnode]
                    
                    if initnode== temp:
                        return True 
                else:
                    return False 
            return True
        posdic= {}
        negdic={}
        n= len(nums)
        for i in range(len(nums)):
            if nums[i]>0:
                mod= (i+nums[i]) % n
                if mod in posdic:
                    
                    if True== traverse(mod, i, posdic):
                        return True
                posdic[i]= mod
            else:
                mod= (i+nums[i])%n
                if mod in negdic:
                    if True == traverse(mod, i, negdic):
                        return True 
                negdic[i]= mod
        return False  