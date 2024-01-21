class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        ans=[0]
        for num in nums:
            ans.append(num+ans[-1])
        
        return ans[1:]