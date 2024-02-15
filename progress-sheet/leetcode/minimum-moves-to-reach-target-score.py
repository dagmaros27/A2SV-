class Solution:
    def minMoves(self, target: int, maxDoubles: int) -> int:
        n = maxDoubles
        rem = 0
        while n > 0 and target >1:
            rem += target % 2
            target = target // 2
            n -= 1
        return target + maxDoubles -n+ rem-1
