class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:
            return 0
        res = 1
        out = 1
        nums = list(sorted(set(nums)))
        for i in range(1,len(nums)):
            if nums[i-1] == nums[i]-1:
                res += 1
            else :
                out = max(res,out)
                res = 1
        

        out = max(res,out)
        return out


