class Solution:
    def wateringPlants(self, plants: List[int], capacity: int) -> int:
        steps=0
        amount=capacity
        for i in range(len(plants)):
            
            if plants[i]>amount:
                steps= steps+  2*(i)
                amount=capacity-plants[i]
            else:
                amount-= plants[i]
            steps+=1
                
        return steps