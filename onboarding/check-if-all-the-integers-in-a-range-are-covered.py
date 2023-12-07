class Solution:
    def isCovered(self, ranges: List[List[int]], left: int, right: int) -> bool:
        
        found = False
        for i in range(left, right+1):
          for r in ranges:
            if r[0] <= i <= r[1]:
                found = True
                break
          if not found:
            return False
          else:
            found = False
        return True