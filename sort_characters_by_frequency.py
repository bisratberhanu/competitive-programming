class Solution:
    from collections import Counter 
    def frequencySort(self, s: str) -> str:
        lis=[]
        for i in s:
            lis.append(i)
        dic= Counter(lis)
        temparray=[]
        for key,value in dic.items():
            temparray.append([key,value])
        #selection sort
        for i in range(len(temparray)):
            maxindex=i
            for j in range(i+1,len(temparray)):
                if temparray[j][1]> temparray[maxindex][1]:
                    maxindex=j
            temparray[i], temparray[maxindex]= temparray[maxindex],temparray[i]
        ans=''
        for i in temparray:
            ans+= i[0]* i[1]
        return ans