class Solution:
    def smallestNumber(self, num: int) -> int:
        if num==0: return 0
        lis=[]
        counter=0
        if num>0:
            numstr= str(num)
            for letter in numstr:
                if letter=='0':
                    counter+=1
                else: lis.append(int(letter))
            lis.sort()
            for i in range(counter):
                lis.insert(1,0)
                print(lis)
            return int(''.join(str(i) for i in lis))
        elif num<0:
            num= abs(num)
            numstr= str(num)
            for letter in numstr:
                if letter=='0':
                    counter+=1
                else: lis.append(int(letter))
            lis.sort(reverse=True)
            lis.extend([0]*counter)
            return -1* int(''.join(str(i) for i in lis))


        