class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        n = len(digits)

        if digits[n-1] == 9:
            self.isnine(n-1, digits)
        else:
            digits[n-1] += 1

        return digits

    def isnine(self, n, arr):
        if arr[n] != 9:
            arr[n] += 1
            return
        else:
            arr[n] = 0
            if n-1 >= 0:
                self.isnine(n-1, arr)
            else:
                arr.insert(0, 1)