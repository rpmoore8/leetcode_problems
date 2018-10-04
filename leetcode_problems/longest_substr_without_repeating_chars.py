"""
//////////////////////////////////////////////
Longest Substring Without Repeating Characters
//////////////////////////////////////////////

Given a string, find the length of the longest substring without repeating characters.

Example 1:
Input: "abcabcbb"
Output: 3 
Explanation: The answer is "abc", with the length of 3. 

Example 2:
Input: "bbbbb"
Output: 1
Explanation: The answer is "b", with the length of 1.

Example 3:
Input: "pwwkew"
Output: 3
Explanation: The answer is "wke", with the length of 3. 
             Note that the answer must be a substring, "pwke" is a subsequence and not a substring.

Difficulty: MEDIUM
"""


class Solution:
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        d = {}
        mx = 0
        tmp = 0
        i = 0

        while i < len(s):
            if s[i] not in d:
                d[s[i]] = i
                i += 1
                tmp += 1
            else:
                mx = max(mx, tmp)
                tmp = 0
                i = d[s[i]] + 1
                d.clear()

        mx = max(mx, tmp)
        return mx
