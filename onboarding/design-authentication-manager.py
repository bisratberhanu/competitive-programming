class AuthenticationManager:

    def __init__(self, timeToLive: int):
        self.dic={}
        self.time_to_live= timeToLive

    def generate(self, tokenId: str, currentTime: int) -> None:
        self.dic[tokenId]=currentTime
        

    def renew(self, tokenId: str, currentTime: int) -> None:
        if tokenId in self.dic and currentTime- self.dic[tokenId]< self.time_to_live: 
            self.dic[tokenId]= currentTime
        

    def countUnexpiredTokens(self, currentTime: int) -> int:
        count=0
        for keys in self.dic:
            if currentTime- self.dic[keys]<self.time_to_live:
                count+=1
        return count        


# Your AuthenticationManager object will be instantiated and called as such:
# obj = AuthenticationManager(timeToLive)
# obj.generate(tokenId,currentTime)
# obj.renew(tokenId,currentTime)
# param_3 = obj.countUnexpiredTokens(currentTime)