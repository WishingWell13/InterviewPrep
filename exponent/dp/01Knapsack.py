'''

https://www.tryexponent.com/practice/prepare/knapsack-problem


Goal: Maximize vvalue

Input: 2 arrays, one integer (max capacity)

Output: Integer representing the max value 

Constrait: Cannot exceeding max capacity

Step:

Add item i:
- Value = value + v[i]
- Capacity = capacity + w[i]

Don't add item i:
- Value = value
- Capacity = capacity

Brute Force:
- Two recursive calls
- O(2^n)

_ _ _ _ _

Dynamic Programming:

Base Case
- totalWeight = 0

- empty items array [], value is 0, weight is 0
- selecting 1 of an item



Memorize:
- totalValue[targetWeight] = max(v[i] + totalValue[targetWeight - w[i]]))

you are frozen on my side

O(C * n)

Keep track of
- Current weight

            A B C
weights = [1, 1, 1]
values = [10, 20, 30]
capacity = 2
output: 50

'''

from typing import List
from collections import defaultdict

def knapsack(weight: List[int], values: List[int], cap: int) -> int:
    if len(weight) == 0:
        return 0
    n = len(weight)
    totalValue = [[0 for _ in range(cap + 1)] for _ in range(n)]

    # Base case, only have one item available
    for c in range(cap + 1):
        print(c)
        if weight[0] <= c:
            totalValue[0][c] = values[0]
            print(f'{c} | {totalValue[0][c]}')

    print(totalValue)

    for i in range(1, len(weight)):
        for remainingCap in range(1, cap+1):
            noPick = totalValue[i-1][remainingCap]
            yesPick = 0

            if remainingCap - weight[i] >= 0:
                yesPick = totalValue[i][remainingCap-weight[i]] + values[i]
            
            totalValue[i][remainingCap] = max(noPick, yesPick)
            print(f'{noPick} {yesPick} {totalValue[i][remainingCap]}')
    
    return totalValue[-1][-1]
        
    
# debug your code below
weights = [60]
values = [100]
capacity = 50
print(knapsack(weights, values, capacity)) 

