"""
/////////////////////////////
Longest Palindromic Substring
/////////////////////////////

Given a string s, find the longest palindromic substring in s. You may assume that the maximum length of s is 1000.

Example 1:
Input: "babad"
Output: "bab"
Note: "aba" is also a valid answer.

Example 2:
Input: "cbbd"
Output: "bb"

Difficulty: MEDIUM
"""


class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        if len(s) == 0:
            return ""

        lp = s[0]
        for i in range(1, len(s)):
            l = i
            r = i
            while l-1 >= 0 and r+1 < len(s) and s[l-1] == s[r+1]:
                l -= 1
                r += 1
            if len(lp) <= r - l:
                lp = s[l:r+1]

            if s[i] == s[i-1]:
                l = i-1
                r = i
                while l-1 >= 0 and r+1 < len(s) and s[l-1] == s[r+1]:
                    l -= 1
                    r += 1
                if len(lp) <= r-l:
                    lp = s[l:r+1]
        return lp
