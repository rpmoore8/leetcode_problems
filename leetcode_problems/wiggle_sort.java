/*
///////////
Wiggle Sort
///////////

Given an unsorted array nums, reorder it in-place such that nums[0] <= nums[1] >= nums[2] <= nums[3]....

Example:

Input: nums = [3,5,2,1,6,4]
Output: One possible answer is [3,5,1,6,2,4]

Difficulty: MEDIUM
*/

class Solution {
    public void wiggleSort(int[] nums) {
        for (int i = 0; i < nums.length; i++) {
            int temp = nums[i];
            int index;
            if (i % 2 == 0)
                index = minIndex(nums, i);
            else
                index = maxIndex(nums, i);

            nums[i] = nums[index];
            nums[index] = temp;
        }
    }

    public int maxIndex(int[] nums, int k) {
        int max = Integer.MIN_VALUE;
        int index = -1;
        for (int i = k; i < nums.length; i++) {
            if (nums[i] > max) {
                max = nums[i];
                index = i;
            }
        }
        return index;
    }

    public int minIndex(int[] nums, int k) {
        int min = Integer.MAX_VALUE;
        int index = -1;
        for (int i = k; i < nums.length; i++) {
            if (nums[i] < min) {
                min = nums[i];
                index = i;
            }
        }
        return index;
    }
}