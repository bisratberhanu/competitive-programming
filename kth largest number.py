def kthLargestNumber(self, nums):
    nlist=[]
    for i in nums:
        nlist.append(int(i))
    nlist.sort(reverse=True)
    return str(nlist[k-1])
        