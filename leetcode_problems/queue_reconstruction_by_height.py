"""
//////////////////////////////
Queue Reconstruction By Height
//////////////////////////////

Suppose you have a random list of people standing in a queue. Each person is described by a pair of integers (h, k), where h is the height of the person and k is the number of people in front of this person who have a height greater than or equal to h. Write an algorithm to reconstruct the queue.

Note:
The number of people is less than 1,100.


Example:
Input:
[[7,0], [4,4], [7,1], [5,0], [6,1], [5,2]]
Output:
[[5,0], [7,0], [5,2], [6,1], [4,4], [7,1]]

Difficulty: MEDIUM
"""


class Solution(object):

    def reconstructQueue(self, people):
        """
        :type people: List[List[int]]
        :rtype: List[List[int]]
        """
        sol = sorted(people, key=lambda x: (x[0]*1101+x[1]))

        for i, x in reversed(list(enumerate(sol))):
            k = 0
            j = i - 1
            while j >= 0 and sol[j][0] >= x[0]:
                k += 1
                j -= 1
            j = i + 1
            while k < x[1]:
                tmp = sol[j]
                sol[j] = sol[j-1]
                sol[j-1] = tmp
                k += 1
                j += 1
            # print(sol)

        return sol
