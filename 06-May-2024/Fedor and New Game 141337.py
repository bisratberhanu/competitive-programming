# Problem: Fedor and New Game - https://codeforces.com/contest/467/problem/B

n,m,k= map(int, input().split())
arr=[]
for _ in range(m+1):
    x= int(input())
    arr.append(x)
    counter=0
fedor= arr[-1]
for i in range(m):
    if bin(arr[i]^fedor).count('1')<= k:
        counter+=1
print(counter)
