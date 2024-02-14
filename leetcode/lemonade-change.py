class Solution:
    def lemonadeChange(self, bills: List[int]) -> bool:
        #greedy 
        five,ten,twenty= 0,0,0
        for bill in bills:
            if bill==5:
                five+=1
            elif bill==10:
                if five:
                    five-=1
                    ten+=1
                else: return False
            else:
                if ten:
                    ten-=1
                    if five:
                        five-=1
                        twenty+=1
                    else: return False
                else:
                    if five>=3:
                        five-=3
                        twenty+=1
                    else: return False
        return True
        

         