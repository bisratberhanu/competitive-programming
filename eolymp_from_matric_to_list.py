from collections import defaultdict
graph= defaultdict(list)
n= int(input())
for i in range(1,n+1):
  line= list(map(int,input().split()))
  
  for j in range(len(line)):
    if line[j]==1:
      graph[i].append(j+1)
for node in graph:
  print(node,end=' ')
  for val in graph[node]:
    print(val,end=' ')
  print()
