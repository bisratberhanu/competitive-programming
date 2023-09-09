vertex= int(input())
operations= int(input())
graph={}
for _ in range(operations):
    kind= list(map(int,input().split()))# kind of operation, 1 or 2
    
    if kind[0]==1:
        a,b= kind[1],kind[2]
        if a not in graph: graph[a]=[]
        if b not in graph: graph[b]=[]
        graph[b].append(a)
        graph[a].append(b)
    else:
        ver=kind[1]
        if ver in graph:
            for neh in graph[ver]:
                print(neh,end=' ')
            print()
        else:
            print()
