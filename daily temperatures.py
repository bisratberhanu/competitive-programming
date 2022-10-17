 def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        ans = [0]*len(temperatures)
        for i in range(len(temperatures)):
            for j in range(i+1, len(temperatures)):
                if temperatures[j] > temperatures[i]:
                    ans[i] = j-i
                    break
        return ans