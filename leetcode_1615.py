class Solution:
    def maximalNetworkRank(self, n: int, roads: List[List[int]]) -> int:
        graph=defaultdict(list)
        for road in roads:
            graph[road[0]].append(road[1])
            graph[road[1]].append(road[0])
        rank=0
        keys=list(graph.keys())
        for key in keys:
            for key2 in keys:
                if key2!=key:
                    temp_rank= len(graph[key])+len(graph[key2])
                    if key2 in graph[key]:
                        temp_rank-=1
                    rank= max(rank,temp_rank)
        return rank

        

        


