class Solution:
    def sequentialDigits(self, low: int, high: int) -> List[int]:
        n, m = len(str(low)), len(str(high))
        res=[]
        def fill(n):
            
            for i in range(1,11-n):
                ch=str(i)
                for j in range(1,n):
                    ch+=str(i+j)
                digit=int(ch)
                if digit>=low and digit <=high:
                    res.append(digit)
        for i in range(n,m+1):
            fill(i)
        return res
        