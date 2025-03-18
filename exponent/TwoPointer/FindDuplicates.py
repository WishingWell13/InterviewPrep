'''
https://www.tryexponent.com/practice/29f6923b-e32d-45e9-a34d-423714bcc8a8

Input: 2 arrays

Output: 1 array with duplicates, ascending order

arr1 = [1, 2, 3, 5, 6, 7]
                          | 

arr2 = [3, 6, 7, 8, 20]
                 | 

Time: O(n + m)
Space: O(1)
'''

from typing import List

def find_duplicates(arr1: List[int], arr2: List[int]) -> List[int]:
    # Maintain two pointers
    p1 = 0
    p2 = 0

    out = []

    # print(len(arr1))
    # print(len(arr2))
    # print('===========')

    # While pointer 1 and pointer 2 haven't reached the end of the array
    while(p1 < len(arr1) and p2 < len(arr2)): 
        # print(f'{p1} {p2}')
        # print(arr1)
        # print(arr2)
        # print('===========')
        # Check if the values at the pointers match. If they do, 
        # increment both pointers and element to our output array
        if arr1[p1] == arr2[p2]:
            out.append(arr1[p1])
            p1 += 1
            p2 += 1
            
        # Increment the pointer pointing to the lower value
        else:
            if arr1[p1] < arr2[p2]: 
                p1 += 1
            else: 
                p2 += 1
    
    return out    

     # your code goes here
  
# debug your code below
print(find_duplicates([1, 2, 3, 5, 6, 7], [3, 6, 7, 8, 20]))

'''
arr1 = [1, 2, 3, 5, 6, 7], arr2 = [3, 6, 7, 8, 20]

'''
