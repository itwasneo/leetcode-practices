'''
Given a string containing just the characters '(' and ')', find the length of the longest valid (well-formed) parentheses substring.

 

Example 1:

Input: s = "(()"
Output: 2
Explanation: The longest valid parentheses substring is "()".
Example 2:

Input: s = ")()())"
Output: 4
Explanation: The longest valid parentheses substring is "()()".
Example 3:

Input: s = ""
Output: 0
 

Constraints:

0 <= s.length <= 3 * 104
s[i] is '(', or ')'.
'''
from typing import List

class Solution:
    def longestValidParentheses(self, s: str) -> int:
        maxAns = 0

        stack = [-1]

        for i in range(len(s)):
            if (s[i] == "("):
                stack.append(i)
            else:
                stack.pop()
                if (len(stack) == 0):
                    stack.append(i)
                else:
                    maxAns = max(maxAns, i - stack[-1])
        return maxAns


if __name__ == "__main__":
    solution = Solution()
    print(solution.longestValidParentheses("(())("))
