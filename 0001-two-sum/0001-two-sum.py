class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        lst={}
        for index,num in enumerate(nums):
            ans=target-num
            if ans in lst:
                return [lst[ans],index]

            lst[num]=index
        return[]        