#https://leetcode.com/problems/delete-operation-for-two-strings/submissions/


from itertools import combinations
from typing import List

def getLongestMatchingWordLenght(x:List,y:List)->int:
    try:
        return len(sorted([word for word in x if word in y],key=len,reverse=True)[0])
    except IndexError:
        return 0

def getCombinationInSequence(word:List[str])->List:
    return ([''.join(word[i:j]) for i,j in combinations(range(len(word)+1),2)])

class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        return(
            len(word1)+len(word2)
            -2*getLongestMatchingWordLenght(
            getCombinationInSequence(list(word1)),
            getCombinationInSequence(list(word2))
            ))
