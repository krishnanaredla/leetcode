# https://leetcode.com/problems/shifting-letters/

class Solution:
    def shiftingLetters(self, s: str, shifts: List[int]) -> str:
        def getL(s):
            if 97 <= s <= 122:
                return s
            else:
                return getL(96+(s-122))
        def getLetter(x,y):
            return chr(getL(ord(x)+sum(y)))
        data = list(map(lambda x : shifts[x:len(shifts)],list(range(len(shifts)))))
        return ''.join(list(map(lambda x,y : getLetter(x,y) ,s,data))) 
