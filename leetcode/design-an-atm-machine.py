class ATM:

    def __init__(self):
        self.arr= [0,0,0,0,0] 
        self.dic={0:20,1:50,2:100,3:200, 4:500}

    def deposit(self, banknotesCount: List[int]) -> None:
        for i in range(5):
            self.arr[i]+= banknotesCount[i]*self.dic[i]
        
    def withdraw(self, amount: int) -> List[int]:
        ans=[0,0,0,0,0]
        copied= self.arr[::]
        for i in range(4,-1,-1):
            if amount< self.dic[i] or self.arr[i]==0:
                continue
            

            val,mod= divmod(amount,self.dic[i])
            if val> self.arr[i]//self.dic[i]:
                ans[i]= self.arr[i]//self.dic[i]
                amount-= self.arr[i]
                self.arr[i]=0
                continue 
            ans[i]= val
            #print(ans)
            amount=mod
            self.arr[i]-= val*self.dic[i]
            if amount==0: return ans   
        if amount!=0: 
            self.arr= copied
            return [-1]
        return ans 


# Your ATM object will be instantiated and called as such:
# obj = ATM()
# obj.deposit(banknotesCount)
# param_2 = obj.withdraw(amount)