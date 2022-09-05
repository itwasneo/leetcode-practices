'''
Implement next permutation, which rearranges numbers into the lexicographically next greater permutation of numbers.

If such an arrangement is not possible, it must rearrange it as the lowest possible order (i.e., sorted in ascending order).

The replacement must be in place and use only constant extra memory.

 

Example 1:

Input: nums = [1,2,3]
Output: [1,3,2]
Example 2:

Input: nums = [3,2,1]
Output: [1,2,3]
Example 3:

Input: nums = [1,1,5]
Output: [1,5,1]
Example 4:

Input: nums = [1]
Output: [1]
 

Constraints:

1 <= nums.length <= 100
0 <= nums[i] <= 100
'''
from typing import List

class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        isNextExist = False

        # If there are only 2 numbers in the array just swap them
        if (len(nums) == 2):
            tmp = nums[1]
            nums[1] = nums[0]
            nums[0] = tmp
            # Saying this is a little bit smelling, for the sorting at the end
            isNextExist = True

        # Iterating nums in reverse order
        for i in range(1, len(nums)):
            # find the first two numbers sequence that is decreasing in reverse order
            if (nums[-i] > nums[-i-1]):
                tmp = nums[-i-1]
                j = (-i-1) + len(nums)

                # find the next number less than or equal to the number that we have found to swap
                while (j+1 < len(nums) and tmp < nums[j+1]):
                    j += 1
                    print(j)
                nums[-i-1] = nums[j]
                nums[j] = tmp

                # reverse the sequence
                reversedSeq = reversed(nums[-i:])
                nums[-i:] = reversedSeq
                isNextExist = True
                break

        if (not isNextExist):
            nums.sort()
        print(nums)

if __name__ == "__main__":
    solution = Solution()
    solution.nextPermutation(nums=[1,2,3])

'''
[1, "2", "4", 3, 2, 1]

[1, "4", "2", 3, 2, 1]

[1, 4, "1, 2, 2, 3"]

[0, 1, 2, 3, 4]
[-5,-4,-3,-2,-1]




'''
