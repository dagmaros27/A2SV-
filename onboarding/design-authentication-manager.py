class AuthenticationManager:

    def __init__(self, timeToLive: int):
        self.time_to_live = timeToLive
        self.tokens = defaultdict(int) # {id: expiretime}
        

    def generate(self, tokenId: str, currentTime: int) -> None:
        self.tokens[tokenId] = currentTime + self.time_to_live

    def renew(self, tokenId: str, currentTime: int) -> None:
        if tokenId in self.tokens:
            if self.tokens[tokenId] <= currentTime:
                del self.tokens[tokenId]
            else:
                self.tokens[tokenId] = currentTime + self.time_to_live
    
    def countUnexpiredTokens(self, currentTime: int) -> int:
        self.tokens = {key: value for key, value in self.tokens.items() if currentTime < value}
    
        
        return len(self.tokens)
        


# Your AuthenticationManager object will be instantiated and called as such:
# obj = AuthenticationManager(timeToLive)
# obj.generate(tokenId,currentTime)
# obj.renew(tokenId,currentTime)
# param_3 = obj.countUnexpiredTokens(currentTime)