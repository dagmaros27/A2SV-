class Solution:
    def minOperations(self, boxes: str) -> List[int]:
        
        ans = []
        for i in range(len(boxes)):
            ops = 0
            for j in range(len(boxes)):
                if i != j and boxes[j] == "1":
                    ops += abs( int(i) - int(j))
            ans.append(ops)

        return ans 
        