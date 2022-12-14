'''
There is an integer array nums sorted in ascending order (with distinct values).

Prior to being passed to your function, nums is rotated at an unknown pivot index k (0 <= k < nums.length) such that the resulting array is [nums[k], nums[k+1], ..., nums[n-1], nums[0], nums[1], ..., nums[k-1]] (0-indexed). For example, [0,1,2,4,5,6,7] might be rotated at pivot index 3 and become [4,5,6,7,0,1,2].

Given the array nums after the rotation and an integer target, return the index of target if it is in nums, or -1 if it is not in nums.

You must write an algorithm with O(log n) runtime complexity.

 

Example 1:

Input: nums = [4,5,6,7,0,1,2], target = 0
Output: 4
Example 2:

Input: nums = [4,5,6,7,0,1,2], target = 3
Output: -1
Example 3:

Input: nums = [1], target = 0
Output: -1
 

Constraints:

1 <= nums.length <= 5000
-104 <= nums[i] <= 104
All values of nums are unique.
nums is guaranteed to be rotated at some pivot.
-104 <= target <= 104
'''
from typing import List


# [4,5,6,7,0,1,2]
class Solution:
    def search(self, nums: List[int], target: int) -> int:
        left = 0
        right = len(nums)-1

        while (left <= right):
            middle = int((left + right) / 2)
            if (nums[middle] == target):
                return middle

            elif (nums[left] <= nums[middle]):
                if (nums[left] <= target <= nums[middle]):
                    right = middle - 1
                else:
                    left = middle + 1

            else:
                if (nums[middle] <= target <= nums[right]):
                    left = middle + 1
                else:
                    right = middle - 1
        return -1






    def search_naive(self, nums: List[int], target: int) -> int:
        # Sanity Checks
        if (len(nums) == 1):
            return 0 if nums[0] == target else -1

        if (target < nums[0] and target > nums[-1]):
            return -1

        if (target == nums[0]):
            return 0

        if (target == nums[-1]):
            return len(nums)-1

        if (target > nums[0]):
            i = 0
            while (i+1 < len(nums) and nums[i] < nums[i+1]):
                if (nums[i] == target):
                    return i
                i += 1
            if (nums[i] == target):
                return i
            return -1

        if (target < nums[-1]):
            i = 1
            while (-i-1 >= -len(nums) and nums[-i-1] < nums[-i]):
                if(nums[-i] == target):
                    return -i+len(nums)
                i += 1
            if(nums[-i] == target):
                return -i+len(nums)
            return -1

if __name__ == "__main__":
    solution = Solution()
    print(solution.search([4, 5, 6, 7, 0, 1, 2], target=0))
