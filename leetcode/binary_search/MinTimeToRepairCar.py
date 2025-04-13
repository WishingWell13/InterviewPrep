'''
Input: Int array representing mechanics

Output: Min time as an integer to repair all cars

rank * number of cars^2

We set n for each mechanic


15 min:

1st: sqrt(t / r) = n cars = sqrt(15 / 4) = 1

https://leetcode.com/problems/minimum-time-to-repair-cars/

'''
class Solution:
    def enoughCars(self, ranks: List[int], cars: int, time):
        carSum = 0

        for rank in ranks:
            carSum += int(sqrt(time / rank))

        print(f'{cars} {time}, {carSum}')
        
        return carSum >= cars

    def repairCars(self, ranks: List[int], cars: int) -> int:
        s = 0

        maxRank = 0
        for rank in ranks:
            maxRank = max(maxRank, rank)
        
        e = (maxRank * pow(cars,2))

        outMin = e 

        # Binary search on time 
        while s <= e:
            mid = int((s + e) / 2)

            # Calculate if enough cars can be created in that time. If we can, update minimum and go left
            if self.enoughCars(ranks, cars, mid):
                outMin = min(mid, outMin)
                e = mid - 1
            # Otherwise, check right side
            else:
                s = mid + 1
        
        return outMin
