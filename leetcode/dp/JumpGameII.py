'''
nums = [2, 5, 5, 5, 5]

dp[i] = minimum number of jumps to get from nums[i] to nums[n-1]

dp[i] = min(dp[i+1]...dp[maxJump])
maxJump = min(i+nums[i], n-1)

Base Case:
i = n-1
dp[n-1] = 0


https://leetcode.com/problems/jump-game-ii/?envType=problem-list-v2&envId=dynamic-programming
'''

class Solution:
    def jump(self, nums: List[int]) -> int:
        dp = [0 for _ in range(len(nums))]
        
        # Base Case
        dp[-1] = 0

        # Iterative step
        for i in range(len(nums)-2, -1, -1):
            jumpRange = nums[i]
            endPoint = min(jumpRange + i, len(nums)-1)

            minJumps = float('inf')

            for j in range(i+1, endPoint+1):
                minJumps = min(minJumps, dp[j] + 1)

            dp[i] = minJumps
        
        return dp[0]
