class Solution:
    def minimumCardPickup(self, cards: List[int]) -> int:
        setter = set()
        l = 0
        min_length = float('inf')
        for r in range(len(cards)):
            while cards[r] in setter:
                min_length = min(min_length, r-l+1)
                setter.discard(cards[l])
                l += 1
            setter.add(cards[r])
        
        return -1 if min_length == float('inf') else min_length
        