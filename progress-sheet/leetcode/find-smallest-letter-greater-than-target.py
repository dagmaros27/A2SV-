class Solution:
    def nextGreatestLetter(self, letters: List[str], target: str) -> str:
        key = lambda x: x > target


        l,h = 0, len(letters)-1

        while l <= h:
            mid = (l+h)//2

            if key(letters[mid]):
                h -= 1
            else:
                l += 1
        return letters[l] if l < len(letters) else letters[0]      