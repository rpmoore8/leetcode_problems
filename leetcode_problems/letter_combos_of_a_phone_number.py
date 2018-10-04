"""
/////////////////////////////////////
Letter Combinations Of A Phone Number
/////////////////////////////////////

Given a string containing digits from 2-9 inclusive, return all possible letter combinations that the number could represent.

A mapping of digit to letters (just like on the telephone buttons) is given below. Note that 1 does not map to any letters.

Example:
Input: "23"
Output: ["ad", "ae", "af", "bd", "be", "bf", "cd", "ce", "cf"].
Note:

Although the above answer is in lexicographical order, your answer could be in any order you want.

Difficulty: MEDIUM
"""


class Solution(object):
    def letterCombinations(self, digits):
        """
        :type digits: str
        :rtype: List[str]
        """
        if len(digits) == 0:
            return []

        d = {"2": "abc", "3": "def", "4": "ghi", "5": "jkl",
             "6": "mno", "7": "pqrs", "8": "tuv", "9": "wxyz"}

        mult = 1
        sect = 1
        for num in digits:
            mult *= len(d[num])

        ans = [[] for x in range(mult)]

        for num in digits:
            sect *= len(d[num])
            i = 0
            k = 0
            while i < mult:
                j = 0
                k %= len(d[num])
                while j < mult//sect:
                    ans[i].append(d[num][k])
                    i += 1
                    j += 1
                k += 1

        strAns = []
        for lst in ans:
            strAns.append("".join(lst))

        return strAns
