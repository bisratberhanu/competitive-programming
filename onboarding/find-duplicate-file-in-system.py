class Solution:
    def findDuplicate(self, paths: List[str]) -> List[List[str]]:
        ans=[]
        dic=defaultdict(list)
        for path in paths:
            main_list= path.split()
            for i  in range(1,len(main_list)):
                lis= main_list[i].split('(')
                temp=main_list[0]
                temp+='/'
                for letter in lis[0]:
                    if letter==' ':
                        temp+='/'
                    else:
                        temp+=letter
                dic[lis[1][0:-1]].append(temp)
        for key in dic:
            if len(dic[key])>1:
                ans.append(dic[key])
        return ans 

