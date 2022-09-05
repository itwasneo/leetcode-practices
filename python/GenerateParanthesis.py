'''
Given n pairs of parentheses, write a function to generate all combinations of well-formed parentheses.

Example 1:

Input: n = 3
Output: ["((()))","(()())","(())()","()(())","()()()"]
Example 2:

Input: n = 1
Output: ["()"]
 

Constraints:

1 <= n <= 8
'''
from typing import List

class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        ans = []

        def back(seq, left, right):
            if (len(seq) == 2 * n):
                ans.append("".join(seq))
                return
            if (left < n):
                seq += "("
                back(seq, left + 1, right)
                seq.pop()
            if (right < left):
                seq += ")"
                back(seq, left, right + 1)
                seq.pop()
            
        back([], 0, 0)
        return ans

if __name__ == "__main__":
    solution = Solution()
    print(solution.generateParenthesis(n = 3))