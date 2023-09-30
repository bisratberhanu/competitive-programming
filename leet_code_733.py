class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        directions= [(1,0),(0,1),(-1,0),(0,-1)]
        visited=set()
        rows,cols= len(image), len(image[0])
        def bfs(image,start,visited):
            queue= deque()
            queue.append(start)
            starting_color= image[start[0]][start[1]]
            image[start[0]][start[1]]=color
            while queue:
                popped= queue.pop()
                row,col= popped[0],popped[1]
                for dr,dc in directions:
                    new_row= row+dr
                    new_col= col+dc
                    if 0<=new_row<rows and 0<=new_col<cols and (new_row,new_col) not in visited and image[new_row][new_col]==starting_color:
                        visited.add((new_row,new_col))
                        queue.appendleft((new_row,new_col))
                        image[new_row][new_col]= color
            return image
        return bfs(image,(sr,sc),visited)





        
