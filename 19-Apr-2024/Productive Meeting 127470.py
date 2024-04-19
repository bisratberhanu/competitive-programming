# Problem: Productive Meeting - https://codeforces.com/contest/1579/problem/D

import heapq

t = int(input())
for _ in range(t):
    n = int(input())
    arr = list(map(int, input().split()))
    arr = [(-arr[i], i+1) for i in range(n) if arr[i] != 0]
    heapq.heapify(arr)
    ans = []

    while len(arr) > 1:
        a = heapq.heappop(arr)
        b = heapq.heappop(arr)
        if a[1]>b[1]:
            ans.append((b[1], a[1]))
        else:
            ans.append((a[1], b[1]))
        if a[0] < -1:
            heapq.heappush(arr, (a[0] + 1, a[1]))
        if b[0] < -1:
            heapq.heappush(arr, (b[0] + 1, b[1]))

    print(len(ans))
    for i in ans:
        print(i[0], i[1])