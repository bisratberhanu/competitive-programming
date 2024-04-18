# Problem: Heap Operations - https://codeforces.com/contest/681/problem/C

import heapq


heap = []
ans= [0]
n= int(input())
for  _ in range(n):
    string= input()
    if string == 'removeMin':
        oper= 'removeMin'
    else:
        oper, val = string.split()
        val = int(val)
    if oper == 'insert':
        heapq.heappush(heap, val)
        ans.append('insert '+str(val))
        
    elif oper=='getMin':
        
        while heap and heap[0] < val:
            heapq.heappop(heap)
            ans.append('removeMin')
            ans[0]+=1
        if not heap or heap[0] > val:
            heapq.heappush(heap, val)
            ans.append('insert '+str(val))
            ans[0]+=1
        ans.append('getMin '+str(val))
    else:
        if not heap:
            heapq.heappush(heap, -10**(9))
            ans.append('insert '+str(-10**(9)))
            ans[0]+=1
        ans.append('removeMin')
        heapq.heappop(heap)
    ans[0]+=1
for val in ans:
    print(val)
