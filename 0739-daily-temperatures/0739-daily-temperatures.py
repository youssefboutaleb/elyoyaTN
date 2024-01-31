class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        seen=[]
        res=[0]*len(temperatures)
        for index,temp in enumerate(temperatures) :
            while seen !=[]:
                i,t=seen[-1]
                if temp>t :
                    res[i]=index-i
                    seen.pop()
                else :
                    break
            seen.append([index,temp])
        return res
            