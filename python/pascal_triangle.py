def factorial(n:int)-int:
    return 1 if (n==1 or n==0) else n * factorial(n - 1);

def PascalFact(n:int,k:int)->int:
    return int(factorial(n)/(factorial(k)*(factorial(n-k))))

class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        return list(map(lambda x:PascalFact(rowIndex,x),list(range(rowIndex+1))))
