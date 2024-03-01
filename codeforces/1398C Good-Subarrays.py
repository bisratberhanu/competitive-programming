# Description: https://codeforces.com/contest/1398/problem/C
t= int(input())
for _ in range(t):
    n= int(input())
    digits= input()
    arr=[]
    count=0 # count of ans
    prefixdict= {0:1} 
    for digit in digits:
        arr.append(int(digit))
    acc=0
    for i, val in enumerate(arr):
        acc+=val-1
        
        if acc in prefixdict:
            count+=prefixdict[acc]
            prefixdict[acc]+=1
        else:
            prefixdict[acc]=1
    print(count)
    
    
