'''
https://leetcode.com/problems/minimum-operations-to-make-binary-array-elements-equal-to-one-i/description/
'''

class Solution:
    def minOperations(self, nums: List[int]) -> int:
        s = 0

        numOp = 0

        while s < len(nums)-2:
            if nums[s] == 0:
                temp = s

                while temp < s + 3:
                    if nums[temp] == 1:
                        nums[temp] = 0
                    else:
                        nums[temp] = 1
                    temp += 1
                
                numOp += 1
                
            s += 1

        if nums[-1] == 0 or nums[-2] == 0:
            return -1
        else:
            return numOp
