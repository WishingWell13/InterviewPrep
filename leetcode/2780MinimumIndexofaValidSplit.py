'''

[1,2,2,2]

[2,1,3,1,1,1,7,1,2,1]

[3,3,3,3,7,2,2]

3 is dominant, 4 threes total

'''
class Solution:
    def getDominantElement(self, nums: List[int]) -> int:
        counts = {}

        # Tuple of (value, count)
        maxVal = -1
        maxCount = -1

        for val in nums:
            counts[val] = counts.get(val, 0) + 1

            if counts[val] >= maxCount:
                maxVal = val
                maxCount = counts[val]
        
        return maxVal, maxCount

    def minimumIndex(self, nums: List[int]) -> int:
        # identify dominant element
        dom, domCount = self.getDominantElement(nums)

        # Identify potential splits
        inFirstArr = 0 # number of dominant elements in the first array
        for i in range(len(nums)):
            if nums[i] == dom:
                inFirstArr += 1
            
            # validity check
            inSecondArr = domCount - inFirstArr
            arrLength2 = len(nums) - 1 - i

            # print(f'{i} {arrLength2} | {inFirstArr} {inSecondArr}')

            if inFirstArr > (i+1) // 2 and inSecondArr > arrLength2 // 2:
                return i

        # If find none are valid, return -1
        return -1
