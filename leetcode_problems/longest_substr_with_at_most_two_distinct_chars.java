/*
///////////////////////////////////////////////////////
Longest Sub String With At Most Two Distinct Characters
///////////////////////////////////////////////////////

Given a string s , find the length of the longest substring t  that contains at most 2 distinct characters.

Example 1:
Input: "eceba"
Output: 3
Explanation: t is "ece" which its length is 3.

Example 2:
Input: "ccaabbb"
Output: 5
Explanation: t is "aabbb" which its length is 5.

Difficulty: HARD
*/

class Solution {
    public int lengthOfLongestSubstringTwoDistinct(String s) {
        if (s.equals(""))
            return 0;

        char ch1 = s.charAt(0);
        char ch2 = '\u0000';
        int maxFront = 0;
        int maxEnd = 0;
        int curFront = 0;
        int curEnd = 0;

        for (int i = 1; i < s.length(); i++) {
            if (s.charAt(i) != ch1) {
                if (ch2 == '\u0000') {
                    ch2 = s.charAt(i);
                    curEnd++;
                } else if (s.charAt(i) != ch2) {
                    if ((curEnd - curFront) > (maxEnd - maxFront)) {
                        maxFront = curFront;
                        maxEnd = curEnd;
                    }
                    i--;
                    curFront = i;
                    curEnd = i;
                    ch1 = s.charAt(curFront);
                    ch2 = '\u0000';
                    while (s.charAt(i) == s.charAt(curFront - 1)) {
                        curFront--;
                    }
                } else {
                    curEnd++;
                }
            } else {
                curEnd++;
            }
        }
        if ((curEnd - curFront) > (maxEnd - maxFront)) {
            maxFront = curFront;
            maxEnd = curEnd;
        }
        return (maxEnd - maxFront + 1);
    }
}