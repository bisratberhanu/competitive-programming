n,k= map(int,input().split())
arr= [[0 for i in range(n)] for i in range(n)]
i=0
for row in arr:
    row[i]=k
    i+=1
for row in arr:
    for val in row:
        print(val, end=" ")
    print()
 