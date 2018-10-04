"""
///////////////////////
Top K Frequent Elements
///////////////////////

Given a non-empty array of integers, return the k most frequent elements.

Example 1:
Input: nums = [1,1,1,2,2,3], k = 2
Output: [1,2]
Example 2:

Input: nums = [1], k = 1
Output: [1]
Note:

You may assume k is always valid, 1 ≤ k ≤ number of unique elements.
Your algorithm's time complexity must be better than O(n log n), where n is the array's size.

Difficulty: MEDIUM
"""


class Solution(object):
    def topKFrequent(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        d = {}

        for n in nums:
            if n not in d:
                d[n] = 1
            else:
                d[n] += 1

        lst = [[] for _ in range(len(nums) + 1)]

        for r, x in d.items():
            lst[x].append(r)

        ans = []

        for i in reversed(lst):
            if i != []:
                for j in i:
                    ans.append(j)
                    k -= 1
                    if k == 0:
                        return ans
