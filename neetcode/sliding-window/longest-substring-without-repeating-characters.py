'''
https://neetcode.io/problems/longest-substring-without-duplicates?list=neetcode150

Input: s = "zxyzxyz"
                s e
Output: 3
'''

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        start = 0
        end = 0 #inclusive
        currChar = set()
        maxLen = 0


        while end < len(s):
            while s[end] in currChar and start < end:
                currChar.remove(s[start])
                start += 1

            currChar.add(s[end])
            maxLen = max(maxLen, end - start + 1)
            end += 1


        return maxLen 
