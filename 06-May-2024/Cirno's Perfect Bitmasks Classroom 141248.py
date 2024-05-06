# Problem: Cirno's Perfect Bitmasks Classroom - https://codeforces.com/problemset/problem/1688/A

from math import log2
t= int(input())

def helper(num):
    if num==1 or num==2:
        print(3)
        return
    if log2(num)== int(log2(num)):
        print(num+1)
        return 
    bit= bin(num)[2:]
    counter=0
    for i in range(len(bit)-1,-1,-1):
        if bit[i]== '1':
            candi= '1' + '0'*(counter)
            if candi!= bit:
                print(int(candi,2))
                return
        counter+=1
    candi= '1' * (len(bit))
    print(int(candi,2))
for _ in range(t):
    n= int(input())
    helper(n)
