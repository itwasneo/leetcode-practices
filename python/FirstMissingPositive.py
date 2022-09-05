'''
Given an unsorted integer array nums, return the smallest missing positive integer.

You must implement an algorithm that runs in O(n) time and uses constant extra space.

 

Example 1:

Input: nums = [1,2,0]
Output: 3
Example 2:

Input: nums = [3,4,-1,1]
Output: 2
Example 3:

Input: nums = [7,8,9,11,12]
Output: 1
 

Constraints:

1 <= nums.length <= 5 * 105
-231 <= nums[i] <= 231 - 1
'''
from typing import List

class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        missingMin = 1
        numsDict = set(nums)

        for i in range(len(nums)):
            if (nums[i] > missingMin or nums[i] <= 0):
                continue
            elif (nums[i] == missingMin):
                missingMin += 1
                while (missingMin in numsDict):
                    missingMin += 1


        return missingMin



if __name__ == "__main__":
    solution = Solution()
    print(solution.firstMissingPositive(
        [2147483647, 2147483646, 2147483645, 3, 2, 1, -1, 0, -2147483648]))
