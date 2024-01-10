class Solution:
    def minimumRecolors(self, blocks: str, k: int) -> int:
        hmap = defaultdict(int)
        min_ops = float('inf')
        l = 0

        for r in range(len(blocks)):
            hmap[blocks[r]] += 1
            if r - l +1 == k:
                min_ops = min(min_ops, hmap['W'])
                hmap[blocks[l]] -= 1
                l += 1
        return min_ops
        

