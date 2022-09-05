'''
Given n non-negative integers representing an elevation map where the width of each bar is 1, compute how much water it can trap after raining.

 

Example 1:


Input: height = [0,1,0,2,1,0,1,3,2,1,2,1]
Output: 6
Explanation: The above elevation map (black section) is represented by array [0,1,0,2,1,0,1,3,2,1,2,1]. In this case, 6 units of rain water (blue section) are being trapped.
Example 2:

Input: height = [4,2,0,3,2,5]
Output: 9
 

Constraints:

n == height.length
1 <= n <= 2 * 104
0 <= height[i] <= 105
'''
from typing import List

class Solution:
    def trap(self, height: List[int]) -> int:
        # 2 POINTERS BEAUTY
        trappedWater, left, right, leftMax, rightMax = 0, 0, len(height) - 1, 0, 0

        while (left < right):
            if (height[left] <= height[right]):
                if (leftMax < height[left]):
                    leftMax = height[left]
                else:
                    trappedWater += leftMax - height[left]
                left += 1
            else:
                if (rightMax < height[right]):
                    rightMax = height[right]
                else:
                    trappedWater += rightMax - height[right]
                right -= 1

        return trappedWater


if __name__ == "__main__":
    solution = Solution()
    print(solution.trap(height=[0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]))
