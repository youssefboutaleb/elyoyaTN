class Solution:
    def divideArray(self, nums: List[int], k: int) -> List[List[int]]:
        nums.sort()
        if len(nums)<3:
            return []
        res=[]
        for i in range(0,len(nums)-2,3):
            if (nums[i+2]-nums[i])<=k:
                res.append([nums[i],nums[i+1],nums[i+2]])
            else :
                return []
        return res