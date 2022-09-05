'''
Given a collection of candidate numbers (candidates) and a target number (target), find all unique combinations in candidates where the candidate numbers sum to target.

Each number in candidates may only be used once in the combination.

Note: The solution set must not contain duplicate combinations.

 

Example 1:

Input: candidates = [10,1,2,7,6,1,5], target = 8
Output: 
[
[1,1,6],
[1,2,5],
[1,7],
[2,6]
]
Example 2:

Input: candidates = [2,5,2,1,2], target = 5
Output: 
[
[1,2,2],
[5]
]
 

Constraints:

1 <= candidates.length <= 100
1 <= candidates[i] <= 50
1 <= target <= 30
'''
from typing import List

class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()

        dic = set()
        sol = []
        n = len(candidates)

        def back(target, idx, cur):
            if (target == 0):
                if (tuple(cur) not in dic):
                    dic.add(tuple(cur))
                    sol.append(list(cur))
                    return
                return
            else:
                for i in range(idx, n):
                    if (i > idx and candidates[i] == candidates[i - 1]):
                        continue

                    if (target - candidates[i] < 0):
                        break
                    
                    cur.append(candidates[i])
                    back(target-candidates[i], i + 1, cur)
                    cur.pop()
        
        back(target, 0, [])
        return sol

if __name__ == "__main__":
    solution = Solution()
    print(solution.combinationSum2(
        [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1,1,1], 27))
