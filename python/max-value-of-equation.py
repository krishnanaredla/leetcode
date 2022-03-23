# Memory limit Exceeded
# https://leetcode.com/problems/max-value-of-equation

from typing import List
from itertools import combinations

class Solution:
    def findMaxValueOfEquation(self, points: List[List[int]], k: int) -> int:
        return max(
                list(
                    map(lambda x : x[0][1]+x[1][1]+ abs(x[0][0]-x[1][0]),
                        [x for x in 
                         list(map(lambda x: x if abs(x[0][0]-x[1][0])<= k else None ,
                              list(combinations(points,2)))) if x is not None])))
        
