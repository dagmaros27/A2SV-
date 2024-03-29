class Solution:
    def corpFlightBookings(self, bookings: List[List[int]], n: int) -> List[int]:
        pf = [0]*(n)

        for i in bookings:
            pf[i[0]-1] += i[2]
            if i[1] < n:
                pf[i[1]] -= i[2]
        for i in range(1,n):
            pf[i] += pf[i-1]
        
        return pf