def largestNumber(self, nums):
    "returns the largest number in the form of string"
    word=''
    for i in nums:
        word+= str(i)
    newl=[]
    for i in word:
        newl.append(i)
    newl.sort(reverse=True)
    result=''
    for i in newl:
        result+=str(i)
    return result
