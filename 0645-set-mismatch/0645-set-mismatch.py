class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        numbers=set(nums)
        for num in range(1,len(nums)+1) :
            if num not in numbers:
                loss=num
                break
        seen=set()
        for num in nums :       
            if num in seen :
                repetition=num
                break
            seen.add(num)
        return [repetition,loss]
        