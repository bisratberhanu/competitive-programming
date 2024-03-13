class Solution:
    def search(self, nums: List[int], target: int) -> int:
        
        def searcher(l,r):
            mid= (l+r)//2
            if nums[mid]== target:
                return mid
            if l>r:
                return -1
            
            if nums[mid]> target:
                return searcher(l, mid-1)
            else:
                return searcher(mid+1, r)
        return searcher(0, len(nums)-1)
        