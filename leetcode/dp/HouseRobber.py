'''
Input: Arr of money values (nonnegative)

Output: Int, max amount of money
               1.2 3 4
Input: nums = [1,2,3,1]


Output: 4

Take 1 -> No 2 -> Take 3 -> No Take 4
Take 1 -> No 2 -> No 3 -> Take 4
Take 1 -> No 2 -> No 3 -> No 4


No 1 -> Take 2
No 1 -> No 2


Input: nums = [2,7,9,3,1]

dp[i] = from nums[i] to the end, what is the max money we can get

nums[i] = max(dp[i+2] + nums[i], dp[i+1])


Base Case:
dp[-1] = nums[-1]
dp[-2] = max(nums[-1], nums[-2])

Output: 12


https://leetcode.com/problems/house-robber/
'''

class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]

        dp = [0 for _ in range(len(nums))]

        # Base Case
        dp[-1] = nums[-1]
        dp[-2] = max(nums[-1], nums[-2])

        for i in range(len(nums)-3, -1, -1):
            # If take currHouse, check currHouse - 2

            # If we don't take currHouse, check currHouse - 1

            dp[i] = max(dp[i+2] + nums[i], dp[i+1])
        
        return dp[0]
        

