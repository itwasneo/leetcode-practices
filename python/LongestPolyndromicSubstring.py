'''
Given a string s, return the longest palindromic substring in s.

 

Example 1:

Input: s = "babad"
Output: "bab"
Note: "aba" is also a valid answer.
Example 2:

Input: s = "cbbd"
Output: "bb"
Example 3:

Input: s = "a"
Output: "a"
Example 4:

Input: s = "ac"
Output: "a"
 

Constraints:

1 <= s.length <= 1000
s consist of only digits and English letters.
'''
from typing import List

class Solution:
    def longestPalindrome(self, s: str) -> str:

        def expand(S, l, r):
            while (l > 0 and r < len(S)-1 and S[l - 1] == S[r + 1]):
                l -= 1
                r += 1
            return S[l:r+1]
        
        maxAns = ""
        for i in range(len(s) - 1):
            L1, L2 = "", ""
            if (s[i] == s[i + 1]):
                L1 = expand(s, i, i + 1)
            L2 = expand(s, i, i)

            if (len(L2) >= len(L1)):
                if (len(L2) > len(maxAns)):
                    maxAns = L2
            else:
                if (len(L1) > len(maxAns)):
                    maxAns = L1

        return maxAns


if __name__ == "__main__":
    solution = Solution()
    print(solution.longestPalindrome(s="babad"))
