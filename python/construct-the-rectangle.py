# :( Time limit Exceeded
# https://leetcode.com/problems/construct-the-rectangle

from typing import List

def getMultiples(n:int)->List:
    data = []
    for i in list(range(1,n+1)):
        for j in list(range(1,n+1)):
            if i*j == n:
                data.append((i,j))
    return [x for x in list(map(lambda x: x if x[0]>=x[1] else None,data)) if x is not None]

class Solution:
    def constructRectangle(self, area: int) -> List[int]:
        data   = list(map(lambda x : {x:x[0]-x[1]} ,getMultiples(area)))
        output = sorted(data, key=lambda key:list(key.values()), reverse=False)
        return list(list(output[0].keys())[0])
        
        
