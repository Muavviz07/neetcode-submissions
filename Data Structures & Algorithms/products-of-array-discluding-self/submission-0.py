class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prefix = 1
        if nums == [] or len(nums) == 1:
            return nums
        
        output = [1]
        for i in nums[:-1]:
            prefix *= i
            output.append(prefix)
        
        pos = len(nums) - 2
        postfix = 1
        i = len(nums) - 1
        while i > 0:
            postfix = postfix * nums[i]
            output[pos] = output[pos] * postfix 

            pos -= 1
            i -= 1


        return(output)

