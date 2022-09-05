'''
Given an array of integers nums sorted in ascending order, find the starting and ending position of a given target value.

If target is not found in the array, return [-1, -1].

You must write an algorithm with O(log n) runtime complexity.

 

Example 1:

Input: nums = [5,7,7,8,8,10], target = 8
Output: [3,4]
Example 2:

Input: nums = [5,7,7,8,8,10], target = 6
Output: [-1,-1]
Example 3:

Input: nums = [], target = 0
Output: [-1,-1]
 

Constraints:

0 <= nums.length <= 105
-109 <= nums[i] <= 109
nums is a non-decreasing array.
-109 <= target <= 109
'''

from typing import List


class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        if (len(nums) == 0):
            return [-1,-1]
        if (len(nums) == 1):
            if (target == nums[0]):
                return [0,0]
            else:
                return [-1,-1]

        left = 0
        right = len(nums) - 1

        while (left <= right):
            middle = int((left + right) / 2)
            if (nums[middle] == target):
                i, j = 1, 1 # Searching how far the range goes from both side
                while (middle - i >= 0 and nums[middle-i] == target):
                    i += 1
                while (middle + j <= len(nums)-1 and nums[middle+j] == target):
                    j += 1
                return [middle-i+1, middle+j-1]

            elif (nums[middle] < target): # target range is on the left side if exists
                left = middle + 1

            else: # target range is on the right side if exists
                right = middle - 1
        return [-1,-1]

        
if __name__ == "__main__":
    solution = Solution()
    print(solution.searchRange([5, 7, 7, 8, 8, 10], 8))
