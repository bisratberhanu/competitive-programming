def fib(self, n: int) -> int:
        l=[0,1]
        if n==0:
            return 0
        for i in range(n-1):
            
            num= l[-1]+ l[-2]
            l.append(num)
        return l[-1]