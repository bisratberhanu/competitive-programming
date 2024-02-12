class Solution:
    def distance(self, nums: List[int]) -> List[int]:
        ans=[]
        index_dic= defaultdict(list)
        dic= defaultdict(int)
        for i in range(len(nums)):
            if len(index_dic[nums[i]])==0:
                index_dic[nums[i]].append(0)
            index_dic[nums[i]].append(index_dic[nums[i]][-1] + i)
        #print(index_dic)
        for i in range(len(nums)):
            index= dic[nums[i]]
            arr= index_dic[nums[i]]
            
        
            before= abs(i*index - arr[index])
            after= abs(arr[-1]- arr[index+1] -((len(arr)-index-2)*i))
            #print(before,after)
            dic[nums[i]]+=1
            tot= before +after 
            ans.append(tot)
        return ans 
            

          
        