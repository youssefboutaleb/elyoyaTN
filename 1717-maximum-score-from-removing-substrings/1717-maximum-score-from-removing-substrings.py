class Solution:
    def maximumGain(self, s: str, x: int, y: int) -> int:
        if x> y :
            pair="ab"
        else :
            pair="ba"
        def remove_pairs(pair,pair_value):
            nonlocal s
            stack =[]
            res=0
            for c in s :
                if c ==pair[1] and stack and pair[0]== stack[-1]:
                    res+=pair_value
                    stack.pop()
                else :
                    stack.append(c)
            s= "".join(stack)
            return res        
        return remove_pairs(pair,max(x,y)) + remove_pairs(pair[::-1],min(x,y))